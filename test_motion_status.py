#Working
import os
SOCKET_INTERFACE = os.getenv('SOCKET_INTERFACE',"false").lower()=='true'
if SOCKET_INTERFACE:
    from neurapy.socket_interface.robot import Robot
else:
    from neurapy.robot import Robot


def test_motion_status():
    r = Robot()
    result = r.motion_status()
    assert result is "IDLE" or "RUNNING" or "POWERED_OFF"