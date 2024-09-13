import os
SOCKET_INTERFACE = os.getenv('SOCKET_INTERFACE',"false").lower()=='true'
if SOCKET_INTERFACE:
    from neurapy.socket_interface.robot import Robot
else:
    from neurapy.robot import Robot

r = Robot()

def test_get_current_joint_angles():
    assert all(isinstance(x, float) for x in r.get_current_joint_angles())

def test_get_current_joint_angles_with_timestamp():
    result = r.get_current_joint_angles_with_timestamp()
    assert isinstance(result[0], list) and isinstance(result[1], float)

def test_get_current_joint_torques():
    assert all(isinstance(x, float) for x in r.get_current_joint_torques())

def test_get_current_joint_torques_with_timestamp():
    result = r.get_current_joint_torques_with_timestamp()
    assert isinstance(result[0], list) and isinstance(result[1], float)

def test_get_current_joint_velocities():
    assert all(isinstance(x, float) for x in r.get_current_joint_velocities())

def test_get_current_joint_velocities_with_timestamp():
    result = r.get_current_joint_velocities_with_timestamp()
    assert isinstance(result[0], list) and isinstance(result[1], float)
