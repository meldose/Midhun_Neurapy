from neurapy.robot import Robot

r = Robot()
circular_property = {
    "speed": 0.25,
    "acceleration": 0.1,
    "jerk": 100,
    "rotation_speed": 1.57,
    "rotation_acceleration": 5.0,
    "rotation_jerk": 100,
    "blending_mode": 2,
    "blend_radius": 0.05,
    "target_pose": [
        [
            0.3744609827431085,
            -0.3391784988266481,
            0.23276604279256016,
            3.14119553565979,
            -0.00017731254047248513,
            -0.48800110816955566
        ],
        [
            0.37116786741831503,
            -0.19686307684994242,
            0.23300456855796453,
            3.141423225402832,
            -0.00020668463548645377,
            -0.48725831508636475
        ],
        [
            0.5190337951593321,
            -0.1969996948428492,
            0.23267853691809767,
            3.1414194107055664,
            -0.00017726201622281224,
            -0.48750609159469604
        ]
    ],
    "store_id":234,
    "current_joint_angles": r.get_current_joint_angles(),
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
plan_id = r.plan_move_circular(**circular_property)
execute = r.executor([plan_id])