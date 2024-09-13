#Working
import os
SOCKET_INTERFACE = os.getenv('SOCKET_INTERFACE',"false").lower()=='true'
if SOCKET_INTERFACE:
    from neurapy.socket_interface.robot import Robot
else:
    from neurapy.robot import Robot

r = Robot()

def test_get_mode():
    result = r.get_mode()
    assert result == "Automatic"
    
def test_get_mode_semi_automatic():
    assert r.switch_to_semi_automatic_mode()
    result = r.get_mode()
    assert result == "SemiAutomatic"