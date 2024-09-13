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
def test_get_analog_input():
    assert r.get_analog_input(0) == -100.0
@pytest.mark.skipif(TEST_ENVIRONMENT != 'HIL_TEST', reason="not HIL_TEST")
def test_get_analog_output():
    assert r.get_analog_output(0) == -100.0

@pytest.mark.skipif(TEST_ENVIRONMENT != 'HIL_TEST', reason="not HIL_TEST")
def test_get_digital_input():
    assert r.get_digital_input(0) == 0

@pytest.mark.skipif(TEST_ENVIRONMENT != 'HIL_TEST', reason="not HIL_TEST")
def test_get_digital_output():
    assert r.get_digital_output(0) == 0
