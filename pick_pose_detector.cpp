#include "pick_pose_detector.hpp"
#include <BoxObjectFlag.hpp>
#include <PickAreaObjectFlag.hpp>
#include <PickPoseObjectFlag.hpp>
#include <iostream>
#include <Components/EcsBoundingBoxInfo.hpp>
#include <BoxInfo.hpp>
#include <PickPoseInfo.hpp>

using namespace ECS_SIM;

ECS_SIM::PickPoseDetector::PickPoseDetector(ECS::EnvironmentModel &em, const ECS::Pose &pickAreaPose, const ECS::Dimensions &pickAreaDimensions) : em(em), pickAreaPose(pickAreaPose), pickAreaDimensions(pickAreaDimensions) 
{ 
    std::cout << "[PickPoseDetector] Constructor" << std::endl;
}


void ECS_SIM::PickPoseDetector::initStaticObjects()
{
    entt::entity pickArea = em.createWorldObject(pickAreaPose, pickAreaDimensions);
    em.reg.emplace<PickAreaObjectFlag>(pickArea);
    em.reg.replace<ECS::BoundingBoxInfo>(pickArea, ECS::BoundingBoxInfo(true, SKYBLUE));
}

void ECS_SIM::PickPoseDetector::runSimulation()
{
    // Clear all exisiting pick poses
    auto pickPoseView = em.reg.view<PickPoseObjectFlag>();
    for (auto pickPose : pickPoseView)
    {
        em.reg.destroy(pickPose);
    }

    // Detect new pick poses
    auto pickAreaView = em.reg.view<raylib::BoundingBox, PickAreaObjectFlag>();
    for (auto pickArea : pickAreaView)
    {
        raylib::BoundingBox pickAreaBBox = pickAreaView.get<raylib::BoundingBox>(pickArea);

        auto boxView = em.reg.view<ECS::Pose, raylib::BoundingBox, BoxObjectFlag, BoxInfo>();
        for (auto box : boxView)
        {
            auto [boxPose, boxBBox, boxInfo] = boxView.get<ECS::Pose, raylib::BoundingBox, BoxInfo>(box);
            if(boxInfo.isTracked || IsBoundingBoxContained(boxBBox, pickAreaBBox))
            {
                ECS::Pose pickPose(Vector3Add(boxPose.position, raylib::Vector3(0.0f, 0.0f, 0.5f)), boxPose.orientation);
                entt::entity pickPoseEntity = em.reg.create();
                em.reg.emplace<ECS::Pose>(pickPoseEntity, pickPose);
                em.reg.emplace<PickPoseObjectFlag>(pickPoseEntity);
                em.reg.emplace<PickPoseInfo>(pickPoseEntity, PickPoseInfo(box));
            }
        }
    }
}

bool ECS_SIM::PickPoseDetector::IsBoundingBoxContained(const BoundingBox& inner, const BoundingBox& outer) {
    return (inner.min.x >= outer.min.x && inner.max.x <= outer.max.x &&
            inner.min.y >= outer.min.y && inner.max.y <= outer.max.y &&
            inner.min.z >= outer.min.z && inner.max.z <= outer.max.z);
}

ECS_SIM::PickPoseDetector::~PickPoseDetector() {}

