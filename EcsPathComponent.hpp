#pragma once

#include "raylib-cpp.hpp"
#include <vector>
#include <math.h>


class EcsPathComponent
{
public:
	EcsPathComponent()
	{
		double lastX = 0.0;
		double lastY = 0.0;
		double scaling = 1.0;
		double step_size = 0.002;
		int steps = 5000;
		double c_scale = 255.0 / steps;
		for (int i = 0.0; i < steps; i += 1)
		{	
			double s = i * step_size;
			double scale = scaling * (0.5 + 0.25 * sin(85.0*s));

			Vector3 p;
			Color c;
			
			p.x = scale*(5.0*(sin(20.0*s) + 0.1 * sin(20.0 * s)) * 20.0 / (s+20));
			p.y = scale*(5.0*(-cos(20.0*s)- 0.1 * cos(20.0 * s)) * 20.0 / (s+20));
			p.z = 10.0*s / 20.0;
			
			c.a = 255;
			c.r = i * c_scale;
			c.g = 255 - i * c_scale;
			c.b = 0;
			
			points.push_back(p);
			phi.push_back(atan2(p.y-lastY,p.x-lastX));
			colors.push_back(c);

			lastX = p.x;
			lastY = p.y;
		}
		phi[0] = phi[1];
	}
	std::vector<Vector3> points;
	std::vector<double> phi;
	std::vector<Color> colors;
};
