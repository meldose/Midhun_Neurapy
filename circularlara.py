yfrom neurapy.robot import Robot

r = Robot()
composite_motion_property = {
    "speed": 0.432,
    "acceleration": 0.2,
    "current_joint_angles": r.robot_status('jointAngles'),
    "commands": [
        {
            "linear": {
                "blend_radius": 0.005,
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
    ]
}
r.move_composite(**composite_motion_property)