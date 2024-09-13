#pragma once

#include "raylib-cpp.hpp"

class EcsModelComponent
{
public:
    Model model;
    Texture2D texture;

    EcsModelComponent() = default;
    EcsModelComponent(const char* modelFile, const char* textureFile)
    {
        model = LoadModel(modelFile);
        texture = LoadTexture(textureFile);
        model.materials[0].maps[MATERIAL_MAP_DIFFUSE].texture = texture;
    }
    EcsModelComponent(const char* modelFile)
    {
        model = LoadModel(modelFile);
    }
    EcsModelComponent(const EcsModelComponent &) = default;
    EcsModelComponent(const Model& model, const Texture2D& texture) : model(model), texture(texture){}
};
