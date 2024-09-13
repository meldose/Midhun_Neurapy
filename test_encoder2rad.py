import os
SOCKET_INTERFACE = os.getenv('SOCKET_INTERFACE',"false").lower()=='true'
if SOCKET_INTERFACE:
    from neurapy.socket_interface.robot import Robot
else:
    from neurapy.robot import Robot

r = Robot()

def test_encoder2rad():
    encoder_ticks = r.robot_status('loadSideEncValue')
    joint_angles = r.encoder2rad(encoder_ticks)
    assert all(isinstance(x, float) for x in joint_angles)
