from neurapy.robot import Robot

r = Robot()
composite_motion_property = {
    "speed": 0.25,
    "acceleration": 0.1,
    "jerk": 100,
    "rotation_speed": 1.57,
    "rotation_acceleration": 5.0,
    "rotation_jerk": 100,
    "blending_mode": 2,
    "blend_radius": 0.005,
    "current_joint_angles": r.get_current_joint_angles(),
    "commands": [
        {
            "linear": {
                "targets": [
                    [
                        -0.000259845199876027,
                        -0.5211437049195536,
                        0.4429382717719519,
                        3.14123272895813,
                        -0.0007908568368293345,
                        -1.570908784866333
                    ],
                    [
                        -0.16633498440272945,
                        -0.5201452059140722,
                        0.4427486025872017,
                        3.140937089920044,
                        -0.0005319403717294335,
                        -1.571555495262146
                    ]
                ]
            }
        },
        {
            "circular": {
                "targets": [
                    [
                        -0.16633498440272945,
                        -0.5201452059140722,
                        0.4427486025872017,
                        3.140937089920044,
                        -0.0005319403717294335,
                        -1.571555495262146
                    ],
                    [
                        -0.16540090985202305,
                        -0.3983552679378624,
                        0.44267608017426174,
                        3.1407113075256348,
                        -0.00036628879024647176,
                        -1.5714884996414185
                    ],
                    [
                        -0.33446498807559716,
                        -0.3989652352814891,
                        0.4421152856242009,
                        3.1402060985565186,
                        0.00030071483342908323,
                        -1.572899580001831
                    ]
                ]
            }
        }
    ],
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
r.move_composite(**composite_motion_property)
r.stop()