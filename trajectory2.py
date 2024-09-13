from neurapy.robot import Robot

r = Robot()
trajectory_motion_property = {
  "current_joint_angles": r.get_current_joint_angles(),
  "timestamps": [
    0.01, 0.02, 0.03
  ],
  "target_joint": [
    [0.0531381, 0.157485, -0.100272, 1.29569, -5.99211e-05, 0.700957,-0.000371511],
    [-0.208897,0.461728,-0.433937,1.66485,-5.99211e-05,0.700382,-0.000383495],
    [0.0120801,0.621298,0.0149563,1.67381,5.99211e-05,0.687403,-0.000359527]
  ]
}
plan_id = r.plan_move_trajectory(**trajectory_motion_property)
execute = r.executor([plan_id])