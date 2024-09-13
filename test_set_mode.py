#Working
import os
SOCKET_INTERFACE = os.getenv('SOCKET_INTERFACE',"false").lower()=='true'
if SOCKET_INTERFACE:
    from neurapy.socket_interface.robot import Robot
else:
    from neurapy.robot import Robot

r = Robot()

def test_mode_teach():
    result=r.set_mode("Teach")
    assert result==True and r.get_mode() == "Teach"



def test_mode_automatic():
    result = r.set_mode("Automatic")
    assert result == True and r.get_mode() == "Automatic"



def test_mode_semi_automatic():
    result = r.set_mode("SemiAutomatic")
    assert result == True and (r.get_mode() == "SemiAutomatic" or r.get_mode() == "Automatic")