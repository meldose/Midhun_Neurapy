import os
SOCKET_INTERFACE = os.getenv('SOCKET_INTERFACE',"false").lower()=='true'
if SOCKET_INTERFACE:
    from neurapy.socket_interface.robot import Robot
else:
    from neurapy.robot import Robot
import pytest

r = Robot()


def test_set_joint_speed():
    joint_speed = 60
    r.set_joint_speed(joint_speed)
    assert r.get_joint_speed() == joint_speed


def test_set_joint_speed_type_error():
    if SOCKET_INTERFACE:
        with pytest.raises(Exception) as err:
            r.set_joint_speed("sixty")
    else:
        with pytest.raises(TypeError) as err:
            r.set_joint_speed("sixty")
    assert str(err.value) == "Speed must be a numeric value (int or float)."


def test_set_joint_speed_value_error_upper():
    if SOCKET_INTERFACE:
        with pytest.raises(Exception) as err:
            r.set_joint_speed(160)
    else:
        with pytest.raises(ValueError) as err:
            r.set_joint_speed(160)
    assert str(err.value) == "Speed must be in the range of 0 to 100."


def test_set_joint_speed_value_error_lower():
    if SOCKET_INTERFACE:
        with pytest.raises(Exception) as err:
            r.set_joint_speed(-6.0)
    else:
        with pytest.raises(ValueError) as err:
            r.set_joint_speed(-6.0)
    assert str(err.value) == "Speed must be in the range of 0 to 100."