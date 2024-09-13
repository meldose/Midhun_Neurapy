#pragma once

#include <raylib.h> // For the Color struct

namespace ECS
{
    struct BoundingBoxInfo {
        bool isVisible;
        Color color;

        BoundingBoxInfo() : isVisible(true), color(RED) {} // Default constructor
        BoundingBoxInfo(bool visibility, Color boxColor) : isVisible(visibility), color(boxColor) {}
    };
}
