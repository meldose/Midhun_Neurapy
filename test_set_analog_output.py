import os
SOCKET_INTERFACE = os.getenv('SOCKET_INTERFACE',"false").lower()=='true'
if SOCKET_INTERFACE:
    from neurapy.socket_interface.robot import Robot
else:
    from neurapy.robot import Robot
import pytest

r = Robot()

@pytest.mark.skipif(r.get_sim_or_real() != 'Real',reason="Not a real robot")
def test_set_analog_output_false():
    r.set_analog_output(1, 0)
    assert r.get_analog_output(1) == 0

@pytest.mark.skipif(r.get_sim_or_real() != 'Real',reason="Not a real robot")
def test_set_analog_output_true():
    r.set_analog_output(1, 2.3)
    assert r.get_analog_output(1) == 2.3

@pytest.mark.skipif(r.get_sim_or_real() != 'Real',reason="Not a real robot")
def test_set_analog_ouput_fail():
    #use an ouput number that does not exist -> Should return False
    num_outputs = r.get_io_configuration()['analog_outputs']
    assert r.set_analog_output(num_outputs, True) == False