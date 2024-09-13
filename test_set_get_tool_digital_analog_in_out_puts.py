import os
TEST_ENVIRONMENT = os.getenv("TEST_ENVIRONMENT","CI/CD").upper()
SOCKET_INTERFACE = os.getenv('SOCKET_INTERFACE',"false").lower()=='true'
if SOCKET_INTERFACE:
    from neurapy.socket_interface.robot import Robot
else:
    from neurapy.robot import Robot
import pytest

r = Robot()

@pytest.mark.skipif(TEST_ENVIRONMENT != 'HIL_TEST', reason="not HIL_TEST")
@pytest.mark.skipif(r.get_sim_or_real() != 'Real',reason="Not a real robot")
def test_set_tool_digital_outputs():
    set_to = [1 for i in range(0, r.get_io_configuration()["tool_digital_outputs"])]
    r.set_tool_digital_outputs(set_to)
    for i in range(0, r.get_io_configuration()["tool_digital_outputs"]):
        assert r.get_tool_digital_output(i) == 1

@pytest.mark.skipif(TEST_ENVIRONMENT != 'HIL_TEST', reason="not HIL_TEST")
def test_get_tool_digital_input():
    for i in range(0, r.get_io_configuration()["tool_digital_inputs"]):
        assert r.get_tool_digital_input(i) == 0.0

def test_get_tool_analog_input():
    for i in range(0, r.get_io_configuration()["tool_analog_inputs"]):
        assert r.get_tool_analog_input(i) == 0.0    
