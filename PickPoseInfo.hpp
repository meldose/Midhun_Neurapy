#pragma once

#include <ecs_main.hpp>

namespace ECS_SIM
{

struct PickPoseInfo {
    entt::entity boxEntity;

    PickPoseInfo(entt::entity boxEntity) : boxEntity(boxEntity) {}
};

}
