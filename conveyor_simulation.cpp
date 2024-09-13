
#include "conveyor_simulation.hpp"
#include <random>
#include <iostream>
#include <Components/EcsModelComponent.hpp>
#include <BoxObjectFlag.hpp>

using namespace ECS_SIM;

ConveyorSimulator::ConveyorSimulator(ECS::EnvironmentModel &em, const ECS::Pose &conveyorPose) : em(em), conveyorPose(conveyorPose)
{
    std::cout << "[ConveyorSimulator] Constructor" << std::endl;
}

void ConveyorSimulator::initStaticObjects()
{
    Vector3 curPos = conveyorPose.position;
    Vector3 vOffset = raylib::Vector3(1.0f, 0.0f, 0.0f);
    ECS::Dimensions dim(raylib::Vector3(-0.5f, 0.0f, -0.5f), raylib::Vector3(0.5f, 0.4f, 0.5f));
    vOffset = Vector3RotateByQuaternion(vOffset, conveyorPose.orientation);
    for (size_t i = 0; i < 4; i++)
    {   
        ECS::Pose curPose(curPos, conveyorPose.orientation);
        em.createModeledObject(curPose, dim, "../Assets/conveyor-stripe-sides.obj");
        curPos = Vector3Add(curPos, vOffset);
    }
    
}

void ConveyorSimulator::runSimulation()
{
    if(this->conveyorRunning)
    {   
        this->conveyorSpeed = getSimulatedConveyorSpeed();
        Vector3 vOffset = raylib::Vector3(conveyorSpeed, 0.0f, 0.0f);
        vOffset = Vector3RotateByQuaternion(vOffset, conveyorPose.orientation);
        // std::cout << "[ConveyorSimulator] Moving conveyor" << std::endl;
        auto boxView = em.reg.view<ECS::Pose, BoxObjectFlag>();
        for (auto box : boxView)
        {
            ECS::Pose boxPose = boxView.get<ECS::Pose>(box);
            boxPose.position = Vector3Add(boxPose.position, vOffset);
            em.updateWorldObjectPose(box, boxPose);
        }
    }
}

float ConveyorSimulator::getSimulatedConveyorSpeed()
{
    return 0.0075f + 0.0075f * sin(GetTime() * 2.0);
}

ConveyorSimulator::~ConveyorSimulator() {}