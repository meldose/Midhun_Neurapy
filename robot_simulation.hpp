#pragma once

#include <ecs_main.hpp>
#include <chrono>

namespace ECS_SIM
{

class RobotSimulator 
{
public:
    RobotSimulator(ECS::EnvironmentModel& em, ECS::Pose initalTcpPose, float robotSpeed);
    ~RobotSimulator();
    
    void initStaticObjects();
    void runSimulation();

    void setTargetPose(const ECS::Pose& target);
    ECS::Pose getCurrentPose() const;

private:
    ECS::EnvironmentModel& em;
    ECS::Pose currentPose;
    ECS::Pose targetPose;
    float robotSpeed; // Units per second
    entt::entity tcpPoseEntity;

    std::chrono::time_point<std::chrono::steady_clock> lastUpdateTime;
    void updateTargetPose();
};

}
