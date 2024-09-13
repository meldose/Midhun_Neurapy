#Working --- but it returns the values, not true or false
import os
SOCKET_INTERFACE = os.getenv('SOCKET_INTERFACE',"false").lower()=='true'
if SOCKET_INTERFACE:
    from neurapy.socket_interface.robot import Robot
else:
    from neurapy.robot import Robot
import pytest
from neurapy.exceptions import IKNotFound

r = Robot()
target_joint_angles=[0.2,0.2,0.2,0.2,0.2,0.2]
end_effector_pose = [0.31937441035446845, 0.07106314399820793, 1.109090727533707, 0.2218226471738111, 0.5592622696480269, 0.672183900379411]
@pytest.mark.skip #function is deprecated
def test_ik_fk():
    target_pose = [round(x,1) for x in r.ik_fk("fk", target_angle = target_joint_angles)]
    target_angle = r.ik_fk("ik", target_pose = end_effector_pose, current_joint = target_joint_angles)
    assert target_pose is not None
    assert target_angle is not None
@pytest.mark.skip #function is deprecated
def test_ik_not_found():
    target_pose = [0.0,0.0,3.0,0.0,0.0,0.0]
    reference_angle = [0.0]*6
    if SOCKET_INTERFACE:
        with pytest.raises(Exception):
            result = r.compute_inverse_kinematics(target_pose,reference_angle)
    else:
        with pytest.raises(IKNotFound):
            result = r.compute_inverse_kinematics(target_pose,reference_angle)