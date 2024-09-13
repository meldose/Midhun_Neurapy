import os
SOCKET_INTERFACE = os.getenv('SOCKET_INTERFACE',"false").lower()=='true'
if SOCKET_INTERFACE:
    from neurapy.socket_interface.robot import Robot
else:
    from neurapy.robot import Robot

r = Robot()

def test_execute_program():
    program_names = r.get_program_names()
    if 'Program_001' in program_names:
        assert r.execute_program("Program_001")
