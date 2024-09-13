import os
import pytest
SOCKET_INTERFACE = os.getenv("SOCKET_INTERFACE","false").lower()=="true"
if SOCKET_INTERFACE:
    from neurapy.socket_interface.robot import Robot
else:
    from neurapy.robot import Robot

r = Robot()
@pytest.mark.skipif(Robot().get_sim_or_real() != 'Real',reason="Not a real robot")
def test_io_get():
	result = r.io("get", io_name = "DO_1")
	assert result == 0
@pytest.mark.skipif(Robot().get_sim_or_real() != 'Real',reason="Not a real robot")
def test_io_get_TID():
    result = r.io("get", io_name="TID_1")
    assert result == 0
@pytest.mark.skipif(Robot().get_sim_or_real() != 'Real',reason="Not a real robot")
def test_io_get_TOD():
    result = r.io("get", io_name="TOD_1")
    assert result == 0
@pytest.mark.skipif(Robot().get_sim_or_real() != 'Real',reason="Not a real robot")
def test_io_get_TIA():
    result = r.io("get", io_name="TIA_1")
    assert result == 0
@pytest.mark.skipif(Robot().get_sim_or_real() != 'Real',reason="Not a real robot")
def test_io_set():
	result = r.io("set", io_name = "DO_2", target_value = True)
	assert result and r.io("get", io_name="DO_2")