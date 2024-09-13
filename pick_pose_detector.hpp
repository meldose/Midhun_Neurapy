#pragma once
#include <ecs_main.hpp>
#include "raylib-cpp.hpp"

namespace ECS_SIM
{

class PickPoseDetector
{
public:
	PickPoseDetector(ECS::EnvironmentModel& em, const ECS::Pose& pickAreaPose, const ECS::Dimensions& pickAreaDimensions);
	~PickPoseDetector();
    void runSimulation();
    void initStaticObjects();
private:
    ECS::EnvironmentModel& em;
    ECS::Pose pickAreaPose;
    ECS::Dimensions pickAreaDimensions;
    bool IsBoundingBoxContained(const BoundingBox& inner, const BoundingBox& outer);
};

}