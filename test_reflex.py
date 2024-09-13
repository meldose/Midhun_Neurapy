import os
SOCKET_INTERFACE = os.getenv('SOCKET_INTERFACE',"false").lower()=='true'
if SOCKET_INTERFACE:
    from neurapy.socket_interface.robot import Robot
else:
    from neurapy.robot import Robot
import pytest
r = Robot()

@pytest.mark.skipif(r.robot_name == 'maira7M',reason="robot doesn't turn off reflex in runner")
def test_disable_reflex():
    r.disable_reflex()
    assert not r.is_reflex_enabled()

@pytest.mark.skipif(r.robot_name == 'maira7M',reason="robot doesn't turn off reflex in runner")
def test_enable_reflex():
    r.disable_reflex()
    r.enable_reflex()
    assert r.is_reflex_enabled()
