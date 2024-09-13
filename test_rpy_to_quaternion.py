import os
SOCKET_INTERFACE = os.getenv('SOCKET_INTERFACE',"false").lower()=='true'
if SOCKET_INTERFACE:
    from neurapy.socket_interface.robot import Robot
else:
    from neurapy.robot import Robot

r = Robot()


def test_rpy_to_quaternion():
    quat = r.rpy_to_quaternion(0,0,0)
    assert quat == [1.0,0,0,0]