#pragma once

#include "Vector3.hpp"

namespace ECS {

struct Dimensions {
    Vector3 min;
    Vector3 max;

    Dimensions() : min(), max() {}
    Dimensions(const Vector3& minCorner, const Vector3& maxCorner) : min(minCorner), max(maxCorner) {}
};

}
