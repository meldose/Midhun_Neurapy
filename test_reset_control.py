import time
import os
SOCKET_INTERFACE = os.getenv('SOCKET_INTERFACE',"false").lower()=='true'
if SOCKET_INTERFACE:
    from neurapy.socket_interface.robot import Robot
else:
    from neurapy.robot import Robot
import pytest

r = Robot()

@pytest.mark.skipif(True,reason="skip till gui part is ready")
def test_reset_control():
    r.reset_control()
    time.sleep(5)
    # this should raise an exception. If it doesn't, the reset did not work.
    with pytest.raises(Exception) as err:
        r.switch_to_automatic_mode()
    # Ensure for the following tests that it waits until connection can be established
    time.sleep(40)
    assert r.switch_to_automatic_mode()