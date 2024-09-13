from neurapy.robot import Robot
import time

r = Robot()
print(r.robot_name)
print(r.dof)
print(r.payload)
r.power_on()

if r.is_robot_in_teach_mode():
    r.switch_to_automatic_mode()
r.set_joint_speed(50)
r.set_joint_acceleration(50)
r.move_joint("Home")
r.move_linear(["Home","Pi1"])
r.set_override(0.2)
r.move_linear(["Pi1", "Pi0"])
r.grasp()
time.sleep(1)
r.move_linear(["Pi0", "Pi1"])
r.set_override(1)
r.move_linear(["Pi1","Pl1"])
r.set_override(0.2)
r.move_linear(["Pl1","Pl0"])
r.release()
time.sleep(1)
r.move_linear(["Pl0","Pl1"])
r.set_override(1)
r.move_linear(["Pl1","Home"])