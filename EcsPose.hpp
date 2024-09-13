
#pragma once

#include <Vector3.hpp>
#include <Vector4.hpp>

namespace ECS
{

struct Pose {
    Vector3 position;
    Quaternion orientation;

    Pose() : position(), orientation() {}
    Pose(const Vector3& pos, const Quaternion& ori) : position(pos), orientation(ori) {}
};

// Overload operator<< to print Pose
inline std::ostream& operator<<(std::ostream& os, const Pose& pose) {
    os << "Position: (" << pose.position.x << ", " << pose.position.y << ", " << pose.position.z << "), ";
    os << "Orientation: (" << pose.orientation.w << ", " << pose.orientation.x << ", " << pose.orientation.y << ", " << pose.orientation.z << ")";
    return os;
}

}