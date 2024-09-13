#Not Working
import os
SOCKET_INTERFACE = os.getenv('SOCKET_INTERFACE',"false").lower()=='true'
if SOCKET_INTERFACE:
    from neurapy.socket_interface.robot import Robot
else:
    from neurapy.robot import Robot
import pytest


@pytest.mark.skipif(Robot().get_sim_or_real() != 'Real',reason="Not a real robot")
def test_gripper_on():
    r = Robot()
    result = r.gripper('on')
    assert result == True
    

@pytest.mark.skipif(Robot().get_sim_or_real() != 'Real',reason="Not a real robot")
def test_gripper_off():
    r = Robot
    result = r.gripper('off')
    assert result == False        
