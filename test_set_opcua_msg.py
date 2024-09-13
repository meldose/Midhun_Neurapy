import os
SOCKET_INTERFACE = os.getenv('SOCKET_INTERFACE',"false").lower()=='true'
if SOCKET_INTERFACE:
    from neurapy.socket_interface.robot import Robot
else:
    from neurapy.robot import Robot

import pytest

@pytest.mark.skipif(Robot().get_sim_or_real() != 'Real',reason="Not a real robot")
def test_set_opcua_msg():
    r = Robot()
    msg = "Hello, OPC UA Server!"
    register_index = 1
    assert r.set_opcua_msg(msg, register_index)
