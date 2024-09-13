from neurapy.robot import Robot
r = Robot()
target_end_effector_pose = [0.140448, -0.134195, 1.197456, 3.1396, -0.589, -1.025]
reference_joint_angles = [-1.55, -0.69, 0.06, 1.67, -0.02, -1.57, 0.11]
joint_angle_solution = r.compute_inverse_kinematics(target_end_effector_pose, reference_joint_angles)