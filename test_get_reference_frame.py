import os
SOCKET_INTERFACE = os.getenv('SOCKET_INTERFACE',"false").lower()=='true'
if SOCKET_INTERFACE:
    from neurapy.socket_interface.robot import Robot
else:
    from neurapy.robot import Robot

r = Robot()

def test_get_reference_frame():
    assert all(isinstance(x, (int, float)) for x in r.get_reference_frame("World"))

def test_get_reference_frame_with_offset(compare_positions):
    offsets = [0.1, 0.2, 0.3]
    r_frame_wit_offsets = r.get_reference_frame_with_offset("World", offsets)
    offsets = offsets + [0 for i in range(0,3)]
    should_be_returned = [a + b for a, b in zip(offsets, r.get_reference_frame("World"))]
    assert compare_positions(should_be_returned, r_frame_wit_offsets)