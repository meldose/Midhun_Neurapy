#working
import os
SOCKET_INTERFACE = os.getenv('SOCKET_INTERFACE',"false").lower()=='true'
if SOCKET_INTERFACE:
    from neurapy.socket_interface.robot import Robot
else:
    from neurapy.robot import Robot

r = Robot()


def test_robot_status_jointangles():
    result = r.robot_status('jointAngles')
    assert result is not None


def test_robot_status_cartesianPosition():
    result = r.robot_status('cartesianPosition')
    assert result is not None

 
def test_robot_status_jointTorques():
    result = r.robot_status('jointTorques')
    assert result is not None 


def test_robot_status_jcommandedjointAngle():
    result = r.robot_status('commandedjointAngle')
    assert result is not None 


def test_robot_status_taskStateTwist():
    result = r.robot_status('taskStateTwist')
    assert result is not None  


def test_robot_status_loadSideEncValue():
    result = r.robot_status('loadSideEncValue')
    assert result is not None 


def test_robot_status_motorSideEncValue():
    result = r.robot_status('motorSideEncValue')
    assert result is not None