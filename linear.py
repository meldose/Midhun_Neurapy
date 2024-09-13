from neurapy.robot import Robot

r = Robot()
linear_property = {
    "speed": 0.25,
    "acceleration": 0.1,
    "rotation_speed": 0.5,
    "blending": True,
    "blending_mode": 2.
    "blend_radius": 0.005,
    "target_pose": [
        [
            0.3287228886,
            -0.1903355329,
            0.4220780352,
            0.08535207028439847,
            -2.797181496822229,
            2.4713321627410485
        ],
        [
            0.2093363791501374,
            -0.31711250784165884,
            0.422149168855134,
            -3.0565555095672607,
            -0.3447442352771759,
            -1.1323236227035522
        ],
        [
            0.2090521916195534,
            -0.5246753336643587,
            0.4218773613553828,
            -3.0569007396698,
            -0.3448921740055084,
            -1.1323626041412354
        ],
        [
            0.3287228886,
            -0.1903355329,
            0.4220780352,
            0.08535207028439847,
            -2.797181496822229,
            2.4713321627410485
        ]
    ],
    "current_joint_angles":  r.get_current_joint_angles(),
    "weaving":False,
    "pattern": 1,
    "amplitude_left": 0.003,
    "amplitude_right": 0.003,
    "frequency": 1.5,
    "dwell_time_left": 0.0,
    "dwell_time_right": 0.0,
    "elevation": 0.0,
    "azimuth": 0.0
}
r.move_linear(**linear_property)
r.stop()