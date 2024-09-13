import os
TEST_ENVIRONMENT = os.getenv("TEST_ENVIRONMENT","CI/CD").upper()
SOCKET_INTERFACE = os.getenv('SOCKET_INTERFACE',"false").lower()=='true'
if SOCKET_INTERFACE:
    from neurapy.socket_interface.robot import Robot
else:
    from neurapy.robot import Robot
import pytest

r = Robot()

@pytest.mark.skipif(TEST_ENVIRONMENT != 'HIL_TEST')
@pytest.mark.skipif(r.get_sim_or_real() != 'Real',reason="Not a real robot")
def test_wait_for_digital_input():
    result = r.wait_for_digital_input(1,10)
    assert result == True
    