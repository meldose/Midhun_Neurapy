#pragma once

#include <ecs_main.hpp>
#include <Components/EcsPose.hpp>

namespace ECS_SIM
{

class ObjectDetectionSimulator
{
public:
	ObjectDetectionSimulator(ECS::EnvironmentModel& em, const ECS::Pose& cameraPose, const Vector3& detectionPosition, const Vector3& detectionSpread);
	~ObjectDetectionSimulator();
    void runSimulation(bool spawnObject);
    void initStaticObjects();
private:
    ECS::EnvironmentModel& em;
    ECS::Pose cameraPose;
    Vector3 detectionPosition;
    Vector3 detectionSpread;
};

}