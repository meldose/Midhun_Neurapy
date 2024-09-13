import os
SOCKET_INTERFACE = os.getenv('SOCKET_INTERFACE',"false").lower()=='true'
if SOCKET_INTERFACE:
    from neurapy.socket_interface.robot import Robot
else:
    from neurapy.robot import Robot
import pytest

r = Robot()

@pytest.mark.skipif(r.get_sim_or_real() != 'Real',reason="Not a real robot")
def test_read_safeio():
    assert r.read_safeio() is True or False
