import os
SOCKET_INTERFACE = os.getenv('SOCKET_INTERFACE',"false").lower()=='true'
if SOCKET_INTERFACE:
    from neurapy.socket_interface.robot import Robot
else:
    from neurapy.robot import Robot
import pytest
import numpy

r = Robot()

joint_angles_lara_8 = [0.2] * r.dof
end_effector_pose_lara_8 = [0.4780166020357496, 0.10388600071424323, 1.63624593624584, 0.2218226471738111, 0.5592622696480269, 0.672183900379411]


@pytest.mark.skipif(Robot().robot_name != 'lara8',reason="Current robot is not lara8")
def test_compute_forward_kinematics(compare_positions):
    computation = r.compute_forward_kinematics(joint_angles_lara_8)
    assert compare_positions(computation, end_effector_pose_lara_8)

@pytest.mark.skipif(Robot().robot_name != 'lara8',reason="Current robot is not lara8")
def test_compute_inverse_kinematics(compare_positions):
    computation = r.compute_inverse_kinematics(end_effector_pose_lara_8, joint_angles_lara_8)
    assert compare_positions(computation, joint_angles_lara_8)


joint_angles_lara_5 = [0.2] * r.dof
end_effector_pose_lara_5 = [0.31937441035446845, 0.07106314399820793, 1.109090727533707, 0.2218226471738111, 0.5592622696480269, 0.672183900379411]


@pytest.mark.skipif(Robot().robot_name != 'lara5',reason="Current robot is not lara5")
def test_compute_forward_kinematics(compare_positions):
    computation = r.compute_forward_kinematics(joint_angles_lara_5)
    assert compare_positions(computation, end_effector_pose_lara_5)

@pytest.mark.skipif(Robot().robot_name != 'lara5',reason="Current robot is not lara5")
def test_compute_inverse_kinematics(compare_positions):
    computation = r.compute_inverse_kinematics(end_effector_pose_lara_5, joint_angles_lara_5)
    assert compare_positions(computation, joint_angles_lara_5)


joint_angles_maira = [0.2] * r.dof
end_effector_pose_maira = [
    0.45402518101132133,
    0.13359825386363777,
    1.8649540267731681,
    0.2577188114189678,
    0.5353988298262191,
    0.8837847704345984,
]

@pytest.mark.skipif(Robot().robot_name != 'maira7M',reason="Current robot is not maira7M")
def test_compute_forward_kinematics(compare_positions):
    computation = r.compute_forward_kinematics(joint_angles_maira)
    assert numpy.allclose(computation, end_effector_pose_maira,0.01,0.01)

@pytest.mark.skipif(Robot().robot_name != 'maira7M',reason="Current robot is not maira7M")
def test_compute_inverse_kinematics(compare_positions):
    computation = r.compute_inverse_kinematics(end_effector_pose_maira, joint_angles_maira)
    assert numpy.allclose(computation, joint_angles_maira,0.01,0.01)
