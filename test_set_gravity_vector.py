import os
TEST_ENVIRONMENT = os.getenv("TEST_ENVIRONMENT","CI/CD").upper()
SOCKET_INTERFACE = os.getenv('SOCKET_INTERFACE',"false").lower()=='true'
if SOCKET_INTERFACE:
    from neurapy.socket_interface.robot import Robot
else:
    from neurapy.robot import Robot
import pytest

r = Robot()


@pytest.mark.skipif(TEST_ENVIRONMENT != 'HIL_TEST', reason="not HIL_TEST")
def test_set_gravity_vector():
    g_vec = [0,0,-9.8]
    r.set_gravity_vector(g_vec)
    res = r.get_gravity_vector()
    assert res['gravity_vector_x'] == g_vec[0] and res['gravity_vector_y'] == g_vec[1] and res['gravity_vector_z'] == g_vec[2]


@pytest.mark.skipif(TEST_ENVIRONMENT != 'HIL_TEST', reason="not HIL_TEST")
def test_set_gravity_vector_value_error():
    with pytest.raises(ValueError) as err:
        r.set_gravity_vector([0, 0, 0, -9.8])
    assert str(err.value) == "Gravity vector length should be 3. provided vector: [0, 0, 0, 9.8]"
    

@pytest.mark.skipif(TEST_ENVIRONMENT != 'HIL_TEST', reason="not HIL_TEST")
def test_set_gravity_vector_value_error_magnitude():
    with pytest.raises(ValueError) as err:
        r.set_gravity_vector([0, 0, -10])
    assert str(err.value) == "Provided gravity vector's magnitude is outside the limits.Magnitude should be in between 9.71 and 9.91 and the provided one is 10.0"
    
