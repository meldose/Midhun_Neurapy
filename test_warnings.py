#working
import os
SOCKET_INTERFACE = os.getenv('SOCKET_INTERFACE',"false").lower()=='true'
if SOCKET_INTERFACE:
    from neurapy.socket_interface.robot import Robot
else:
    from neurapy.robot import Robot


def test_warnings():
    r = Robot()
    result = r.get_warnings() # returns list of warning codes(floats)
    assert result is None