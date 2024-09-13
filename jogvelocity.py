import time
from neurapy.robot import Robot
r = Robot()

'''
jog_velocity - velocity ranging from [-1,1] for all joints. Signifies percentage of total speed used (1 = 100%)
jog_type - can be either cartesian or joint jogging
turn_on_jog sets the parameters of external jogging, jogging velocity, jogging type and sets the mode for jogging to external mode.
'''
r.turn_on_jog(jog_velocity=[0.2, 0.2, 0.2, 0.2, 0.2, 0.2], jog_type='Joint')
r.jog(set_jogging_external_flag=1)
i = 0
'''
Requires minimum number of cycles in the loop for performing jogging.
Depends upon jogging velocity, override.
'''
while i < 500:
    #command to set flag to start jogging in external mode. This command has to be used each time external jog command has to be sent
    r.jog(set_jogging_external_flag=1)
    i += 1

#Command to switch back to internal jogging mode (GUI)
r.turn_off_jog()