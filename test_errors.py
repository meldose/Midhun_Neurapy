#Working
import os
SOCKET_INTERFACE = os.getenv('SOCKET_INTERFACE',"false").lower()=='true'
if SOCKET_INTERFACE:
    from neurapy.socket_interface.robot import Robot
else:
    from neurapy.robot import Robot
import pytest

r = Robot()

def test_notify_error():
    assert r.notify_error("Something went wrong!")

def test_error_with_no_errors():
    result = r.get_errors()
    assert result == None

@pytest.mark.skip
def test_error_with_errors():
    # TODO call function_to_create_an_error()
    r.notify_error("Something went wrong!")
    result = r.get_errors()
    assert result == "Something went wrong!"

def test_reset_errors():
    r.notify_error("Something went wrong!")
    r.reset_errors()
    errors = r.get_errors()
    assert errors == None
