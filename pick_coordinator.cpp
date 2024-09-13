#include "pick_coordinator.hpp"
#include <BoxObjectFlag.hpp>
#include <PickAreaObjectFlag.hpp>
#include <PickPoseObjectFlag.hpp>
#include <iostream>
#include <TargetPoseObjectFlag.hpp>
#include <TcpPoseObjectFlag.hpp>
#include <PickStageObjectFlag.hpp>
#include <PickPoseInfo.hpp>
#include <BoxInfo.hpp>

using namespace ECS_SIM;

ECS_SIM::PickCoordinator::PickCoordinator(ECS::EnvironmentModel &em, const ECS::Pose& idlePose, const ECS::Pose& placePose) : em(em), idlePose(idlePose), placePose(placePose)
{ 
    std::cout << "[PickCoordinator] Constructor" << std::endl;
}

const char* ECS_SIM::getPickStageString(PickStage stage) {
    switch (stage) {
        case PickStage::WAITING: return "WAITING";
        case PickStage::MOVING_TO_PRE_PICK: return "MOVING_TO_PRE_PICK";
        case PickStage::MOVING_TO_PICK: return "MOVING_TO_PICK";
        case PickStage::WAITING_FOR_GRIP: return "WAITING_FOR_GRIP";
        case PickStage::MOVING_TO_POST: return "MOVING_TO_POST";
        case PickStage::MOVING_TO_PLACE: return "MOVING_TO_PLACE";
        case PickStage::WAITING_FOR_RELEASE: return "WAITING_FOR_RELEASE";
        default: return "UNKNOWN";
    }
}

void ECS_SIM::PickCoordinator::initStaticObjects()
{
    targetPoseEntity = em.reg.create();
    em.reg.emplace<ECS::Pose>(targetPoseEntity, idlePose);
    em.reg.emplace<TargetPoseObjectFlag>(targetPoseEntity);
    pickStageEntity = em.reg.create();
    em.reg.emplace<PickStage>(pickStageEntity, pickStage);
    em.reg.emplace<PickStageObjectFlag>(pickStageEntity);
}

ECS::Pose* PickCoordinator::tryToTrackBox(const Vector3& lastBoxToTrackPosition) {
    ECS::Pose* bestBoxPose = nullptr;
    float minDistance = std::numeric_limits<float>::max();

    entt::entity bestBoxEntity = entt::null;

    auto pickPoseView = em.reg.view<ECS::Pose, PickPoseObjectFlag, PickPoseInfo>();
    for (auto pickPose : pickPoseView) 
    {
        auto [pickPosePose, pickPoseInfo] = pickPoseView.get<ECS::Pose, PickPoseInfo>(pickPose);

        BoxInfo curBoxInfo = em.reg.get<BoxInfo>(pickPoseInfo.boxEntity);
        curBoxInfo.isTracked = false;
        em.reg.replace<BoxInfo>(pickPoseInfo.boxEntity, curBoxInfo);

        float distance = Vector3Distance(lastBoxToTrackPosition, pickPosePose.position);
        if (distance < minDistance) 
        {
            minDistance = distance;
            bestBoxPose = &pickPosePose;
            bestBoxEntity = pickPoseInfo.boxEntity;
        }
    }
    // std::cout << "minDistance = " << minDistance << std::endl;

    if (bestBoxPose && minDistance < sameBoxDistThreshold) 
    {
        if(bestBoxEntity != entt::null)
        {
            BoxInfo curBoxInfo = em.reg.get<BoxInfo>(bestBoxEntity);
            curBoxInfo.isTracked = true;
            em.reg.replace<BoxInfo>(bestBoxEntity, curBoxInfo);
        }
        return bestBoxPose;
    } 
    else 
    {
        return nullptr;
    }
}

ECS::Pose* PickCoordinator::getBoxToTrackPose() {
    ECS::Pose* bestPose = nullptr;
    float maxX = -std::numeric_limits<float>::max();

    auto pickPoseView = em.reg.view<ECS::Pose, PickPoseObjectFlag, PickPoseInfo>();
    for (auto pickPose : pickPoseView) {
        auto [pickPosePose, pickPoseInfo] = pickPoseView.get<ECS::Pose, PickPoseInfo>(pickPose);

        BoxInfo curBoxInfo = em.reg.get<BoxInfo>(pickPoseInfo.boxEntity);
        curBoxInfo.isTracked = false;
        em.reg.replace<BoxInfo>(pickPoseInfo.boxEntity, curBoxInfo);

        if (pickPosePose.position.x < newBoxMaxX && pickPosePose.position.x > maxX) {
            maxX = pickPosePose.position.x;
            bestPose = &pickPosePose;
        }
    }

    return bestPose;
}

void ECS_SIM::PickCoordinator::runStateMachine()
{
    auto tcpPoseView = em.reg.view<ECS::Pose, TcpPoseObjectFlag>();
    ECS::Pose tcpPose;
    for (auto tcpPoseEntity : tcpPoseView)
    {
        tcpPose = tcpPoseView.get<ECS::Pose>(tcpPoseEntity);
        break;
    }

    ECS::Pose* trackedBoxPose = nullptr;
    bool gripper_closed = true;
    bool gripper_open = true;

    switch (pickStage) {
        case PickStage::WAITING:
            targetPose = idlePose;
            trackedBoxPose = getBoxToTrackPose();
            if (trackedBoxPose != nullptr) {
                boxToTrackPose = ECS::Pose(trackedBoxPose->position, trackedBoxPose->orientation);
                std::cout << "[WAITING] Detected box to track, transitioning to MOVING_TO_PRE_PICK" << std::endl;
                pickStage = PickStage::MOVING_TO_PRE_PICK;
            }
            break;

        case PickStage::MOVING_TO_PRE_PICK:
            trackedBoxPose = tryToTrackBox(boxToTrackPose.position);
            if(trackedBoxPose != nullptr)
            {
                boxToTrackPose = ECS::Pose(trackedBoxPose->position, trackedBoxPose->orientation);
                if (Vector3Distance(tcpPose.position, Vector3Add(boxToTrackPose.position, approachOffset)) < targetReachedThreshold) {
                    pickStage = PickStage::MOVING_TO_PICK;
                    std::cout << "[MOVING_TO_PRE_PICK] Reached target, transitioning to MOVING_TO_PICK" << std::endl;
                } else {
                    targetPose.position = Vector3Add(boxToTrackPose.position, approachOffset);
                }
            } 
            else 
            {
                pickStage = PickStage::WAITING;
                std::cout << "[MOVING_TO_PRE_PICK] Lost box to track, transitioning to WAITING" << std::endl;
            }

            break;

        case PickStage::MOVING_TO_PICK:
            trackedBoxPose = tryToTrackBox(boxToTrackPose.position);
            if(trackedBoxPose != nullptr)
            {
                boxToTrackPose = ECS::Pose(trackedBoxPose->position, trackedBoxPose->orientation);
                if (Vector3Distance(tcpPose.position, boxToTrackPose.position) < targetReachedThreshold) {
                    pickStage = PickStage::WAITING_FOR_GRIP;
                    std::cout << "[MOVING_TO_PICK] Reached target, transitioning to WAITING_FOR_GRIP" << std::endl;
                } else {
                    targetPose.position = boxToTrackPose.position;
                }
            } 
            else 
            {
                pickStage = PickStage::WAITING;
                std::cout << "[MOVING_TO_PICK] Lost box to track, transitioning to WAITING" << std::endl;
            }
            break;

        case PickStage::WAITING_FOR_GRIP:
            // TODO: Add logic to check if the box has been grasped
            if (gripper_closed) {
                pickStage = PickStage::MOVING_TO_POST;
                std::cout << "[WAITING_FOR_GRIP] Box grasped, transitioning to MOVING_TO_POST" << std::endl;
            }
            break;

        case PickStage::MOVING_TO_POST:
            trackedBoxPose = tryToTrackBox(boxToTrackPose.position);
            if(trackedBoxPose != nullptr)
            {
                boxToTrackPose = ECS::Pose(trackedBoxPose->position, trackedBoxPose->orientation);
                if (Vector3Distance(tcpPose.position, Vector3Add(boxToTrackPose.position, approachOffset)) < targetReachedThreshold) {
                    pickStage = PickStage::MOVING_TO_PLACE;
                    std::cout << "[MOVING_TO_POST] Target reached, transitioning to MOVING_TO_PLACE" << std::endl;
                } else {
                    targetPose.position = Vector3Add(boxToTrackPose.position, approachOffset);
                }
            }
            else 
            {
                pickStage = PickStage::WAITING;
                std::cout << "[MOVING_TO_POST] Lost box to track, transitioning to WAITING" << std::endl;
                throw std::runtime_error("Lost box to track when moving to post, this shouldn't happen!");
            }

            break;

        case PickStage::MOVING_TO_PLACE:
            if (Vector3Distance(tcpPose.position, placePose.position) < targetReachedThreshold) {
                pickStage = PickStage::WAITING_FOR_RELEASE;
                std::cout << "[MOVING_TO_PLACE] Target reached, transitioning to WAITING_FOR_RELEASE" << std::endl;
            } else {
                targetPose.position = placePose.position;
            }
            break;

        case PickStage::WAITING_FOR_RELEASE:
            // TODO: Add logic to check if the box has been released
            if (gripper_open) {
                pickStage = PickStage::WAITING;
                std::cout << "[WAITING_FOR_RELEASE] Box released, transitioning to WAITING" << std::endl;
            }
            break;

    }
    em.reg.replace<PickStage>(pickStageEntity, pickStage);
}

void ECS_SIM::PickCoordinator::runSimulation()
{
    runStateMachine();

    // std::cout << "[PickCoordinator] targetPose = " << targetPose << std::endl;
    em.reg.replace<ECS::Pose>(targetPoseEntity, targetPose);
}

ECS_SIM::PickCoordinator::~PickCoordinator() {}

