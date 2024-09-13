#include "raylib-cpp.hpp"
#include <vector>
#include <random>

class EcsPickPattern
{
public:
	EcsPickPattern()
	{
		std::random_device rd; // obtain a random number from hardware
		std::mt19937 gen(rd()); // seed the generator
		std::uniform_int_distribution<> distr(-1000, 1000); // define the range
		float scale = 3.0;
		for (int i = 0; i < 100; i++)
		{
			Vector3 p;
			p.x = (float)distr(gen) * scale / 1000.0f;
			p.y = (float)distr(gen) * scale / 1000.0f;
			p.z = (float)distr(gen) * scale / 1000.0f;
			points.push_back(p);
		}
	}
	std::vector<Vector3> points;
};