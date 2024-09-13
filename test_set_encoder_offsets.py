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
def test_set_encoder_offsets():
    enc_offsets = r.get_encoder_offsets()
    new_enc_offsets = [0.2] * len(enc_offsets)
    r.set_encoder_offsets(new_enc_offsets)
    assert new_enc_offsets == r.get_encoder_offsets()

@pytest.mark.skipif(TEST_ENVIRONMENT != 'HIL_TEST', reason="not HIL_TEST")
def test_set_encoder_offsets_value_error_lower():
    enc_offsets = r.get_encoder_offsets()
    new_enc_offsets = [0.2] * (len(enc_offsets) - 1)
    with pytest.raises(ValueError) as err:
        r.set_encoder_offsets(new_enc_offsets)
    assert "Length of provided encoder offsets list is not equal to the number of joints on the robot." in str(err.value)
    
@pytest.mark.skipif(TEST_ENVIRONMENT != 'HIL_TEST', reason="not HIL_TEST")
def test_set_encoder_offsets_value_error_upper():
    enc_offsets = r.get_encoder_offsets()
    new_enc_offsets = [0.2] * (len(enc_offsets) + 1)
    with pytest.raises(ValueError) as err:
        r.set_encoder_offsets(new_enc_offsets)
    assert "Length of provided encoder offsets list is not equal to the number of joints on the robot." in str(err.value)