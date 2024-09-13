import os
SOCKET_INTERFACE = os.getenv('SOCKET_INTERFACE',"false").lower()=='true'
if SOCKET_INTERFACE:
    from neurapy.socket_interface.robot import Robot
else:
    from neurapy.robot import Robot

r = Robot()

def test_get_current_tool_cogs():
    assert all(isinstance(x, (int, float)) for x in r.get_current_tool_cogs())

def test_get_current_tool_inertias():
    assert all(isinstance(x, (int, float)) for x in r.get_current_tool_inertias())

def test_get_current_tool_mass():
    assert isinstance(r.get_current_tool_mass(), (int, float))

def test_get_current_tool_properties():
    assert all(isinstance(x, (int, float)) for x in r.get_current_tool_properties())

def test_get_current_tool_rpy_offsets():
    assert all(isinstance(x, (int, float)) for x in r.get_current_tool_rpy_offsets())

def test_get_current_tool_translation_offsets():
    assert all(isinstance(x, (int, float)) for x in r.get_current_tool_translation_offsets())
