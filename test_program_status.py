#Working
import os
SOCKET_INTERFACE = os.getenv('SOCKET_INTERFACE',"false").lower()=='true'
if SOCKET_INTERFACE:
    from neurapy.socket_interface.robot import Robot
else:
    from neurapy.robot import Robot
import threading
import time

# def test_program_status():    
#     r = Robot()
#     result = r.program_status()
#     assert result is "RUNNING" or "PAUSED" or "NOT_RUNNING"

def test_program_status():
    def run_program():
        r.execute_program("Program_001")
    r = Robot()
    # before executing a program the program_status should be "NOT_RUNNING"
    assert r.program_status() is "NOT_RUNNING"
    if "Program_001" in r.get_program_names():
        # start thread that runs a program
        executor_thread = threading.Thread(target=run_program)
        executor_thread.start()

        time.sleep(1)
        try:
            # during execution of a program the program_status should be "RUNNING"
            assert r.program_status() is "RUNNING"

            time.sleep(1)
            r.pause()

            # when pausing the program_status should be "PAUSED"
            assert r.program_status() is "PAUSED"

            r.unpause()
            time.sleep(1)

            # after unpausing the program_status should be "RUNNING" again
            assert r.program_status() is "RUNNING"

        finally: 
            executor_thread.join()

            # Finally when the program has terminated the program_status should be "NOT_RUNNING"
            assert r.program_status() is "NOT_RUNNING"
