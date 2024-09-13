import os
SOCKET_INTERFACE = os.getenv('SOCKET_INTERFACE',"false").lower()=='true'
if SOCKET_INTERFACE:
    from neurapy.socket_interface.robot import Robot
else:
    from neurapy.robot import Robot

r = Robot()

def test_get_tcp_pose():
    result = r.get_tcp_pose()
    assert all(isinstance(x, float) for x in result) 
    assert len(result) == 6 

def test_get_tcp_pose_with_timestamp():
    result, timestamp = r.get_tcp_pose_with_timestamp()
    assert all(isinstance(x, float) for x in result) and len(result) == 6 and isinstance(timestamp, float)
    
def test_get_tcp_pose_quaternion():
    quaternion = r.get_tcp_pose_quaternion()
    assert all(isinstance(x, float) for x in quaternion) and len(quaternion) == 7
    
def test_get_tcp_pose_quaternion_with_timestamp():
    quaternion, timestamp = r.get_tcp_pose_quaternion_with_timestamp()
    assert all(isinstance(x, float) for x in quaternion) and len(quaternion) == 7 and isinstance(timestamp, float)
    
def test_tcp_pose_change_on_tool_change(compare_positions):
    # flange pose should stay the same even if a tool is set
    flange_pos_1 = r.get_tcp_pose()
    tool_changed = False
    assert r.set_tool(tool_name="RobotiQ")
    assert not compare_positions(flange_pos_1, r.get_tcp_pose())