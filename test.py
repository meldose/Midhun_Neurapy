from neurapy.robot import Robot
import time  
import numpy
import numpy as np
r = Robot()
joint_property = {
    "speed": 50.0,
    "acceleration": 50.0,
    "safety_toggle": True,
    "target_joint": [
        [
            2.5995838308821924,
            0.24962416292345468,
            -1.8654403327490414,
            0.04503286318691005,
            -1.1740563715454926,
            0.10337461241185522
        ],
        [
            2.1372059994827075,
            0.24939733788589463,
            -1.8651270179353125,
            0.044771940725327274,
            -1.173860821592129,
            0.10315646291502645
        ],
        [
            1.9180047887810003,
            -0.24855170101601043,
            -1.3680228668892351,
            0.12404421791100637,
            -1.1914147150222498,
            -0.13255713717112075
        ]
    ],
    "current_joint_angles":  r.get_current_joint_angles()
}
r.move_joint(**joint_property)
r.stop()