import os
SOCKET_INTERFACE = os.getenv('SOCKET_INTERFACE',"false").lower()=='true'
if SOCKET_INTERFACE:
    from neurapy.socket_interface.robot import Robot
else:
    from neurapy.robot import Robot

def test_list_recorded_path():
    r = Robot()
    result = r.list_recorded_path()
    assert isinstance(result, list)
