import os
SOCKET_INTERFACE = os.getenv('SOCKET_INTERFACE',"false").lower()=='true'
if SOCKET_INTERFACE:
    from neurapy.socket_interface.robot import Robot
else:
    from neurapy.robot import Robot

r = Robot()


def test_notify_warning():
    assert r.notify_warning("This is a warning!")


def test_notify_warning_fail():
    assert r.notify_warning(1234567) == False

