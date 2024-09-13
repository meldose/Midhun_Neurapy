#pragma once

namespace ECS_SIM
{
    struct BoxInfo {
        bool isTracked;
        bool isPicked;

        BoxInfo() : isTracked(false), isPicked(false) {} // Default constructor
        BoxInfo(bool isTracked, bool isPicked) : isTracked(isTracked), isPicked(isPicked) {}
    };
}
