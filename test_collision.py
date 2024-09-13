import os
SOCKET_INTERFACE = os.getenv('SOCKET_INTERFACE',"false").lower()=='true'
if SOCKET_INTERFACE:
    from neurapy.socket_interface.robot import Robot
else:
    from neurapy.robot import Robot

r = Robot()


def test_disable_collision_detection():
    r.disable_collision_detection()
    assert not r.is_collision_enabled()


def test_enable_collision_detection():
    r.disable_collision_detection()
    r.enable_collision_detection()
    assert r.is_collision_enabled()
