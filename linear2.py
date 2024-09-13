from neurapy.robot import Robot

r = Robot()
linear_property = {
    "speed": 0.25,
    "acceleration": 0.1,
    "jerk": 100,
    "rotation_speed": 1.57,
    "rotation_acceleration": 5.0,
    "rotation_jerk": 100,
    "blending": True,
    "blending_mode": 1,
    "blend_radius": 0.005,
    "target_pose": [
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
r.move_linear_from_current_position(**linear_property)
r.stop() 