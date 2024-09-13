#include "robot_simulation.hpp"
#include <iostream> // For debug output
#include <TargetPoseObjectFlag.hpp>
#include <TcpPoseObjectFlag.hpp>

using namespace ECS_SIM;

ECS_SIM::RobotSimulator::RobotSimulator(ECS::EnvironmentModel& em, ECS::Pose initalTcpPose, float robotSpeed)
    : em(em), currentPose(initalTcpPose), robotSpeed(robotSpeed), lastUpdateTime(std::chrono::steady_clock::now()) 
{
    targetPose = ECS::Pose();
}

void ECS_SIM::RobotSimulator::initStaticObjects()
{
    tcpPoseEntity = em.reg.create();
    em.reg.emplace<ECS::Pose>(tcpPoseEntity, currentPose);
    em.reg.emplace<TcpPoseObjectFlag>(tcpPoseEntity);
}

void ECS_SIM::RobotSimulator::runSimulation()
{
    updateTargetPose();

    auto now = std::chrono::steady_clock::now();
    std::chrono::duration<float> elapsed = now - lastUpdateTime;
    float deltaTime = elapsed.count();
    lastUpdateTime = now;

    // Calculate distance between currentPose and targetPose
    float distance = Vector3Distance(targetPose.position, currentPose.position);

    // If the distance is very small, we can assume we've reached the target
    if (distance < 0.001f) 
    {
        currentPose = targetPose;
        return;
    }

    // Calculate the interpolation factor
    float distanceToMove = robotSpeed * deltaTime;
    float factor = distanceToMove / distance;

    if (factor >= 1.0f) 
    {
        currentPose = targetPose; // We've reached the target
    } 
    else 
    {
        // Interpolate position
        currentPose.position.x += factor * (targetPose.position.x - currentPose.position.x);
        currentPose.position.y += factor * (targetPose.position.y - currentPose.position.y);
        currentPose.position.z += factor * (targetPose.position.z - currentPose.position.z);

        // Interpolate orientation (quaternion slerp)
        currentPose.orientation = QuaternionSlerp(currentPose.orientation, targetPose.orientation, factor);
    }

    em.reg.replace<ECS::Pose>(tcpPoseEntity, currentPose);
}

void ECS_SIM::RobotSimulator::updateTargetPose()
{
    auto targetPoseView = em.reg.view<ECS::Pose, TargetPoseObjectFlag>();
    for(auto targetPoseEntity : targetPoseView)
    {
        auto targetPose = targetPoseView.get<ECS::Pose>(targetPoseEntity);
        this->setTargetPose(targetPose);
        break;
    }
}

void ECS_SIM::RobotSimulator::setTargetPose(const ECS::Pose& target) 
{
    targetPose = target;
}

ECS::Pose ECS_SIM::RobotSimulator::getCurrentPose() const 
{
    return currentPose;
}

ECS_SIM::RobotSimulator::~RobotSimulator() {}