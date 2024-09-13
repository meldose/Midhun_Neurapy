import os
SOCKET_INTERFACE = os.getenv('SOCKET_INTERFACE',"false").lower()=='true'
if SOCKET_INTERFACE:
    from neurapy.socket_interface.robot import Robot
else:
    from neurapy.robot import Robot

r = Robot()

def test_get_current_load_side_encoder_values():
    assert all(isinstance(x, float) for x in r.get_current_load_side_encoder_values())

def test_get_current_load_side_encoder_values_with_timestamp():
    result = r.get_current_load_side_encoder_values_with_timestamp()
    assert isinstance(result[0], list) and isinstance(result[1], float)