
#include "object_detection_simulation.hpp"
#include <random>
#include <iostream>
#include <BoxObjectFlag.hpp>
#include <BoxInfo.hpp>

using namespace ECS_SIM;

ObjectDetectionSimulator::ObjectDetectionSimulator(ECS::EnvironmentModel &em, const ECS::Pose &cameraPose, const Vector3 &detectionPosition, const Vector3 &detectionSpread) : em(em), cameraPose(cameraPose), detectionPosition(detectionPosition), detectionSpread(detectionSpread)
{
    std::cout << "[ObjectDetectionSimulator] Constructor" << std::endl;
}

void ObjectDetectionSimulator::initStaticObjects()
{
    ECS::Dimensions dim(raylib::Vector3(-0.2f, 0.0f, -0.2f), raylib::Vector3(0.2f, 0.3f, 0.2f));
    em.createModeledObject(cameraPose, dim, "../Assets/can.glb");
}

void ObjectDetectionSimulator::runSimulation(bool spawnObject)
{
    if (spawnObject)
    {
        std::random_device rd;                              // obtain a random number from hardware
        std::mt19937 gen(rd());                             // seed the generator
        std::uniform_int_distribution<> distr(-1000, 1000); // define the range
        Vector3 spawnPos;
        spawnPos.x = (float)distr(gen) * detectionSpread.x / 1000.0f;
        spawnPos.y = (float)distr(gen) * detectionSpread.y / 1000.0f;
        spawnPos.z = (float)distr(gen) * detectionSpread.z / 1000.0f;
        spawnPos = Vector3Add(spawnPos, detectionPosition);
        ECS::Pose spawnPose(spawnPos, QuaternionFromEuler(PI/2.0f, 0.0f, 0.0f));
        ECS::Dimensions dim(raylib::Vector3(-0.25f, 0.0f, -0.25f), raylib::Vector3(0.25f, 0.5f, 0.25f));
        // std::cout << "Spawning object at (" << spawnPos.x << ", " << spawnPos.y << ", " << spawnPos.z << ")" << std::endl;
        entt::entity box = em.createModeledObject(spawnPose, dim, "../Assets/box-small.obj");
        em.reg.emplace<BoxObjectFlag>(box);
        em.reg.emplace<BoxInfo>(box, BoxInfo(false, false));
    }
}

ObjectDetectionSimulator::~ObjectDetectionSimulator() {}