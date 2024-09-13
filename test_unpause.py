import os
SOCKET_INTERFACE = os.getenv('SOCKET_INTERFACE',"false").lower()=='true'
if SOCKET_INTERFACE:
    from neurapy.socket_interface.robot import Robot
else:
    from neurapy.robot import Robot


def test_unpause():
    r = Robot()
    status = r.program_status()
    if status != "PAUSED":
        r.pause()
    r.unpause()
    status = r.program_status()
    assert status != "PAUSED"
