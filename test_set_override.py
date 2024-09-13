import os
SOCKET_INTERFACE = os.getenv('SOCKET_INTERFACE',"false").lower()=='true'
if SOCKET_INTERFACE:
    from neurapy.socket_interface.robot import Robot
else:
    from neurapy.robot import Robot
import pytest

r = Robot()


def test_set_override():
    override = 1
    r.set_override(override)
    assert override == r.get_override()

def test_set_override_type_error():
    if SOCKET_INTERFACE:
        with pytest.raises(Exception) as err:
            r.set_override("0.7")
    else:
        with pytest.raises(TypeError) as err:
            r.set_override("0.7")
    assert str(err.value) == "'<=' not supported between instances of 'float' and 'str'"

def test_set_override_value_error_upper():
    if SOCKET_INTERFACE:
        with pytest.raises(Exception) as err:
            r.set_override(1.1)
    else:
        with pytest.raises(ValueError) as err:
            r.set_override(1.1)
    assert str(err.value) == "Invalid Override value"

def test_set_override_value_error_lower():
    if SOCKET_INTERFACE:
        with pytest.raises(Exception) as err:
            r.set_override(-0.7)
    else:
        with pytest.raises(ValueError) as err:
            r.set_override(-0.7)
    assert str(err.value) == "Invalid Override value"