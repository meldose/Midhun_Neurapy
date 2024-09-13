#pragma once

#include <ecs_main.hpp>
#include <Components/EcsPose.hpp>

namespace ECS_SIM
{

class ConveyorSimulator
{
public:
	ConveyorSimulator(ECS::EnvironmentModel& em, const ECS::Pose& conveyorPose);
	~ConveyorSimulator();
    void runSimulation();
    void initStaticObjects();
    bool getConveyorRunning() const { return conveyorRunning; }
    void setConveyorRunning(bool conveyorRunning_) { conveyorRunning = conveyorRunning_; }
    float getConveyorSpeed() const { return conveyorSpeed; }
    void setConveyorSpeed(float conveyorSpeed_) { conveyorSpeed = conveyorSpeed_; }
private:
    ECS::EnvironmentModel& em;
    ECS::Pose conveyorPose;
    float conveyorSpeed = 0.01f;
    bool conveyorRunning = true;
    float getSimulatedConveyorSpeed();
};

}