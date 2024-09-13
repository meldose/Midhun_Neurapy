#Working
import os
SOCKET_INTERFACE = os.getenv('SOCKET_INTERFACE',"false").lower()=='true'
if SOCKET_INTERFACE:
    from neurapy.socket_interface.robot import Robot
else:
    from neurapy.robot import Robot

r = Robot()

def test_override_set():
    override = 0.5
    result = r.override('set', target_value = override)
    assert result == True and r.get_override() == override


def test_override_get():
    result = r.override('get')
    assert result == 0.5