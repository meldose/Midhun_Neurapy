from neurapy.robot import Robot
r = Robot()
composite_motion_property = {
    "acceleration": 0.1,
    "jerk": 100,
    "rotation_acceleration": 5.0,
    "rotation_jerk": 100,
    "blending_mode": 2,
    "blend_radius": 0.005,
    "current_joint_angles": r.get_current_joint_angles(),
    "use_children_velocities": True,
    "commands": [
        {
            "linear": {
                "targets": [
                    [
                        0.7006,
                        0.0001,
                        0.6875,
                        3.1416,
                        0,
                        3.1416
                    ],
                    [
                        0.7006,
                        0.0001,
                        0.6875,
                        3.1416,
                        0,
                        3.1416
                    ],
                    [
                        0.7509102896938852,
                        0.27460943971123764,
                        0.6864972996055627,
                        3.141592653589793,
                        -7.71435533383267e-06,
                        -3.1415926535897882
                    ],
                    [
                        0.7747260445464177,
                        0.15721988912449852,
                        0.8931631506500376,
                        -3.1415926535897745,
                        -7.714355718231237e-06,
                        -3.1415926535897354
                    ],
                    [
                        0.7006,
                        0.0001,
                        0.6875,
                        3.1416,
                        0,
                        3.1416
                    ]
                ],
                "velocity": 0.1,
                "rotation_velocity": 0.174533
            }
        },
        {
            "circular": {
                "targets": [
                    [
                        0.7006,
                        0.0001,
                        0.6875,
                        3.1416,
                        0,
                        3.1416
                    ],
                    [
                        0.6999986609380567,
                        -0.25149522267751856,
                        0.6864972999318248,
                        -3.141592653589793,
                        -7.71435539238761e-06,
                        3.1415926535897905
                    ],
                    [
                        0.7747260445464177,
                        0.15721988912449852,
                        0.8931631506500376,
                        -3.1415926535897745,
                        -7.714355718231237e-06,
                        -3.1415926535897354
                    ]
                ],
                "velocity": 0.4,
                "rotation_velocity": 0.436332
            }
        }
    ],
    "weaving": False
}
r.move_composite(composite_motion_property)
r.stop()