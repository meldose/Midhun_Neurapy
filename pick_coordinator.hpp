#pragma once
#include <ecs_main.hpp>
#include "raylib-cpp.hpp"

namespace ECS_SIM
{

enum class PickStage {
    WAITING,
    MOVING_TO_PRE_PICK,
    MOVING_TO_PICK,
    WAITING_FOR_GRIP,
    MOVING_TO_POST,
    MOVING_TO_PLACE,
    WAITING_FOR_RELEASE
};
const char* getPickStageString(PickStage stage);

class PickCoordinator
{
public:
	PickCoordinator(ECS::EnvironmentModel& em, const ECS::Pose& idlePose, const ECS::Pose& placePose);
	~PickCoordinator();
    void runSimulation();
    void initStaticObjects();

private:
    ECS::EnvironmentModel& em;
    ECS::Pose idlePose; // pose the robot stays at if there are no boxes to pick
    ECS::Pose placePose; // pose to place the box at
    ECS::Pose targetPose; // current target pose for the robot
    ECS::Pose boxToTrackPose; // pose of box to currently track
    entt::entity targetPoseEntity;
    entt::entity pickStageEntity;

    PickStage pickStage = PickStage::WAITING;
    void runStateMachine();

    ECS::Pose* tryToTrackBox(const Vector3& lastBoxToTrackPosition);
    ECS::Pose* getBoxToTrackPose();
    const float sameBoxDistThreshold = 0.02f;
    const float newBoxMaxX = 1.8f;

    const Vector3 approachOffset = {0.0f, 0.0f, 0.5f};
    const float targetReachedThreshold = 0.02f;
};

}