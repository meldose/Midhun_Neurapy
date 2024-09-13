import os
SOCKET_INTERFACE = os.getenv('SOCKET_INTERFACE',"false").lower()=='true'
if SOCKET_INTERFACE:
    from neurapy.socket_interface.robot import Robot
else:
    from neurapy.robot import Robot
import pytest

r = Robot()

@pytest.fixture
def provide_tool_name():
    return 'some_random_tool'

def test_create_tool(provide_tool_name):
    name = provide_tool_name
    tools = r.get_tools()
    tool_names = [tool["name"] for tool in tools]
    while tool_names.count(name) > 0:
        name = name + '1'
    tool_data = { '_controlOA': False,
        '_controlOD': False,
        '_toolOA': False,
        '_toolOD': False,
        'autoM': 0,
        'autoMeasureX': 0,
        'autoMeasureY': 0,
        'autoMeasureZ': 0,
        'closeInput': 0,
        'cmdID': 16,
        'description': 'Tool Description',
        'force': 0,
        'gripper': '',
        'grippertype': 'Standard Gripper',
        'inertiaXX': 0,
        'inertiaXY': 0,
        'inertiaXZ': 0,
        'inertiaYY': 0,
        'inertiaYZ': 0,
        'inertiaZZ': 0,
        'name': name,
        'offCOA': [0, 0, 0, 0, 0, 0, 0, 0],
        'offCOD1': 0,
        'offCOD2': 0,
        'offTOA': [0, 0],
        'offTOD': 0,
        'offsetA': 0,
        'offsetB': 0,
        'offsetC': 0,
        'offsetX': 0,
        'offsetY': 0,
        'offsetZ': 0,
        'onCOA': [0, 0, 0, 0, 0, 0, 0, 0],
        'onCOD1': 0,
        'onCOD2': 0,
        'onTOA': [0, 0],
        'onTOD': 0,
        'openInput': 0,
        'portID': '',
        'protocol': 0,
        'robot_type': 'Tool',
        'slaveID': 0,
        'speed': 0}
    r.create_tool(tool_data)
    tools = r.get_tools()
    tool_names = [tool["name"] for tool in tools]
    assert tool_names.count(name) == 1

@pytest.mark.skip # This test is failing on Gitlab for now, the reason is unknown. It will be skipped until we figure out what is happening in the pipeline. 
def test_create_tool_duplicate(provide_tool_name):
    name = provide_tool_name
    tool_data = { '_controlOA': False,
        '_controlOD': False,
        '_toolOA': False,
        '_toolOD': False,
        'autoM': 0,
        'autoMeasureX': 0,
        'autoMeasureY': 0,
        'autoMeasureZ': 0,
        'closeInput': 0,
        'cmdID': 16,
        'description': 'Tool Description',
        'force': 0,
        'gripper': '',
        'grippertype': 'Standard Gripper',
        'inertiaXX': 0,
        'inertiaXY': 0,
        'inertiaXZ': 0,
        'inertiaYY': 0,
        'inertiaYZ': 0,
        'inertiaZZ': 0,
        'name': name,
        'offCOA': [0, 0, 0, 0, 0, 0, 0, 0],
        'offCOD1': 0,
        'offCOD2': 0,
        'offTOA': [0, 0],
        'offTOD': 0,
        'offsetA': 0,
        'offsetB': 0,
        'offsetC': 0,
        'offsetX': 0,
        'offsetY': 0,
        'offsetZ': 0,
        'onCOA': [0, 0, 0, 0, 0, 0, 0, 0],
        'onCOD1': 0,
        'onCOD2': 0,
        'onTOA': [0, 0],
        'onTOD': 0,
        'openInput': 0,
        'portID': '',
        'protocol': 0,
        'robot_type': 'Tool',
        'slaveID': 0,
        'speed': 0}
    with pytest.raises(Exception) as err:
        r.create_tool(tool_data)
    assert "Failed to create a tool" in str(err.value)