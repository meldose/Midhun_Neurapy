import os
SOCKET_INTERFACE = os.getenv('SOCKET_INTERFACE',"false").lower()=='true'
if SOCKET_INTERFACE:
    from neurapy.socket_interface.robot import Robot
else:
    from neurapy.robot import Robot

r = Robot()

def test_switch_to_automatic_mode():
    r.set_mode("Teach")
    result = r.switch_to_automatic_mode()
    assert result and r.get_mode() == "Automatic"
