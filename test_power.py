#Working
from time import sleep
import os
SOCKET_INTERFACE = os.getenv('SOCKET_INTERFACE',"false").lower()=='true'
if SOCKET_INTERFACE:
    from neurapy.socket_interface.robot import Robot
else:
    from neurapy.robot import Robot
import pytest

r = Robot()


@pytest.mark.skipif(Robot().get_sim_or_real() != 'Real',reason="Not a real robot")
def test_power_on():
    result = r.power('off')
    sleep(2)
    assert result == True and r.motion_status() == 'POWERED_OFF'

@pytest.mark.skipif(Robot().get_sim_or_real() != 'Real',reason="Not a real robot")
def test_power_off():
    result = r.power('on')
    sleep(2)
    assert result == True and r.motion_status() == 'NOT_RUNNING'
@pytest.mark.skipif(r.robot_name == 'maira7M',reason="robot doesn't turn off power in runner") #robot doesn't turn off power in runner
def test_power_power_off():
    result = r.power_off()
    sleep(2)
    assert result and r.motion_status() == 'POWERED_OFF'

def test_power_power_on():
    r.power_off()
    sleep(2)
    result = r.power_on()
    sleep(2)
    assert result and r.motion_status() == 'NOT_RUNNING'
