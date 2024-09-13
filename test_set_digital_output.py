import os
SOCKET_INTERFACE = os.getenv('SOCKET_INTERFACE',"false").lower()=='true'
if SOCKET_INTERFACE:
    from neurapy.socket_interface.robot import Robot
else:
    from neurapy.robot import Robot
import pytest

r = Robot()

@pytest.mark.skipif(r.get_sim_or_real() != 'Real',reason="Not a real robot")
def test_set_digital_output_false():
    r.set_digital_output(1, False)
    assert r.get_digital_output(1) == 0

@pytest.mark.skipif(r.get_sim_or_real() != 'Real',reason="Not a real robot")
def test_set_digital_output_true():
    r.set_digital_output(1, True)
    assert r.get_digital_output(1) == 1

@pytest.mark.skipif(r.get_sim_or_real() != 'Real',reason="Not a real robot")
def test_set_digital_output_fail():
    #use an output number that does not exist -> Should return False
    num_outputs = r.get_io_configuration()['digital_outputs']
    assert r.set_digital_output(num_outputs, True) == False
@pytest.mark.skipif(r.get_sim_or_real() != 'Real',reason="Not a real robot")
def test_set_digital_output_type_error1():
    if SOCKET_INTERFACE:
        with pytest.raises(Exception) as err:
            r.set_digital_output("1", True)
    else: 
        with pytest.raises(TypeError) as err:
            r.set_digital_output("1", True)
    assert str(err.value) == "Io_name must be an int value!"
@pytest.mark.skipif(r.get_sim_or_real() != 'Real',reason="Not a real robot")
def test_set_digital_output_type_error2():
    if SOCKET_INTERFACE:
        with pytest.raises(Exception) as err:
            r.set_digital_output(1, 1)
    else:
        with pytest.raises(TypeError) as err:
            r.set_digital_output(1, 1)
    assert str(err.value) == "Target_value must be a boolean value!"