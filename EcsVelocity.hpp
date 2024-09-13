#pragma once
#include <Vector3.hpp>

namespace ECS
{

struct Velocity {
    Vector3 value;

    Velocity() : value() {}
    Velocity(const Vector3& val) : value(val) {}
};

}