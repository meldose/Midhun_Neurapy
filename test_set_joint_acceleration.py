import os
SOCKET_INTERFACE = os.getenv('SOCKET_INTERFACE',"false").lower()=='true'
if SOCKET_INTERFACE:
    from neurapy.socket_interface.robot import Robot
else:
    from neurapy.robot import Robot
import pytest

r = Robot()


def test_set_joint_acceleration():
    acceleration = 60
    r.set_joint_acceleration(acceleration)
    assert r.get_joint_acceleration() == acceleration


def test_set_joint_acceleration_type_error():
    if SOCKET_INTERFACE:
        with pytest.raises(Exception) as err:
            r.set_joint_acceleration("sixty")
    else:
        with pytest.raises(TypeError) as err:
            r.set_joint_acceleration("sixty")
    assert str(err.value) == "Acceleration must be a numeric value (int or float)."


def test_set_joint_acceleration_value_error_upper():
    if SOCKET_INTERFACE:
        with pytest.raises(Exception) as err:
            r.set_joint_acceleration(160)
    else:
        with pytest.raises(ValueError) as err:
            r.set_joint_acceleration(160)
    assert str(err.value) == "Acceleration must be in the range of 0 to 100."


def test_set_joint_acceleration_value_error_lower():
    if SOCKET_INTERFACE:
        with pytest.raises(Exception) as err:
            r.set_joint_acceleration(-6.0)
    else:
        with pytest.raises(ValueError) as err:
            r.set_joint_acceleration(-6.0)
    assert str(err.value) == "Acceleration must be in the range of 0 to 100."