import os
SOCKET_INTERFACE = os.getenv('SOCKET_INTERFACE',"false").lower()=='true'
if SOCKET_INTERFACE:
    from neurapy.socket_interface.robot import Robot
else:
    from neurapy.robot import Robot

r = Robot()

def test_get_io_configuration():
    io_config = r.get_io_configuration()
    assert isinstance(io_config['analog_inputs'], int)
    assert isinstance(io_config['analog_outputs'], int)
    assert isinstance(io_config['digital_inputs'], int)
    assert isinstance(io_config['digital_outputs'], int)
    assert isinstance(io_config['tool_analog_inputs'], int)
    assert isinstance(io_config['tool_digital_inputs'], int)
    assert isinstance(io_config['tool_digital_outputs'], int)
