#pragma once
#include <Vector3.hpp>

namespace ECS
{

struct Acceleration {
    Vector3 value;

    Acceleration() : value() {}
    Acceleration(const Vector3& val) : value(val) {}
};

}