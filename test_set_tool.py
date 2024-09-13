# working -setting tool gives result as False
import os
SOCKET_INTERFACE = os.getenv('SOCKET_INTERFACE',"false").lower()=='true'
if SOCKET_INTERFACE:
    from neurapy.socket_interface.robot import Robot
else:
    from neurapy.robot import Robot
import pytest
import numpy

r = Robot()
tool_name = "RobotiQ"

def test_set_tool():
    result = r.set_tool(tool_name=tool_name)
    assert result and r.current_tool == tool_name

def test_set_tool_error():
    with pytest.raises(TypeError) as err:
        r.set_tool("RobotiQ")
    assert "Please provide a tool" in str(err.value)

def test_update_tool_parameters():
    result = r.update_tool_parameters(tool_name=tool_name, offsetZ=0.1, autoM=0.5)
    robotiq_params = [element for element in r.get_tools() if element["name"] == "RobotiQ"][0]
    assert result and robotiq_params["offsetZ"] == 0.1 and robotiq_params["autoM"] == 0.5

def test_update_tool_parameters_error():
    with pytest.raises(TypeError) as err:
        r.update_tool_parameters(offsetZ=0.1, autoM=0.5)
    assert "Missing tool_name" in str(err.value)

def test_update_current_tool_parameters():
    result = r.update_current_tool_parameters(offsetZ=0.3, autoM=0.7)
    assert result and 0.3 in r.tool_params and 0.7 in r.tool_params

def test_update_current_tool_parameters_error():
    with pytest.raises(TypeError) as err:
        r.update_current_tool_parameters(tool_name="somerandomtool", offsetZ=0.1, autoM=0.5)
    assert "Do not provide tool_name" in str(err.value)

def test_if_set_in_orocos_and_ik_server():
    tol = 1e-04
    # First compute some forward kinematics with NoTool
    r.set_tool(tool_name="NoTool")
    target = [1.0] * r.dof
    fw_no_tool = r.compute_forward_kinematics(target)
    
    # Compare result when a tool is equipped -> should be different 
    r.set_tool(tool_name="RobotiQ")
    fw_robotiq = r.compute_forward_kinematics(target)
    assert not numpy.allclose(fw_robotiq, fw_no_tool, rtol=tol, atol=tol)
    
    # Do the same when updating 
    r.update_current_tool_parameters(offsetX=0.7, offsetY=0.5)
    assert not numpy.allclose(r.compute_forward_kinematics(target), fw_robotiq, rtol=tol, atol=tol)
    
    # Reset the RobotiQ tool to the initial state (change database back to default)
    r.update_tool_parameters(tool_name="RobotiQ", offsetX=0.0, offsetY=0.0, offsetZ=0.21, offsetA=0.0, offsetB=0.0, offsetC=0.0, autoM=0.2)
    r.set_tool(tool_name="NoTool")

def test_set_load():
    r.set_tool(tool_name=tool_name)
    load_mass=0.2
    result = r.set_load(load_mass=load_mass, load_cog_x=0.02, load_cog_y=0.03, load_cog_z=0.04)
    robotiq_params = [element for element in r.get_tools() if element["name"] == "RobotiQ"][0]
    
    # Robotiq has no rotation, so can add the translation from flange to tcp and tcp to cog of load
    load_cog_in_flange_frame = [0.02 + robotiq_params['offsetX'], 0.03 + robotiq_params['offsetY'] , 0.04 + robotiq_params['offsetZ']] 

    assert result and result[0]==(robotiq_params['autoM'] + 0.2) 
    assert result[7]==((robotiq_params['autoMeasureX'] * robotiq_params['autoM']  + load_cog_in_flange_frame[0] * load_mass)/result[0])
    assert result[8]==((robotiq_params['autoMeasureY'] * robotiq_params['autoM']  + load_cog_in_flange_frame[1] * load_mass)/result[0])
    assert result[9]==((robotiq_params['autoMeasureZ'] * robotiq_params['autoM']  + load_cog_in_flange_frame[2] * load_mass)/result[0])

def test_remove_load():
    result = r.remove_load()
    robotiq_params = [element for element in r.get_tools() if element["name"] == "RobotiQ"][0]

    assert result and result[0]==(robotiq_params['autoM']) 
    assert result[7]==(robotiq_params['autoMeasureX'])
    assert result[8]==(robotiq_params['autoMeasureY'])
    assert result[9]==(robotiq_params['autoMeasureZ'])

# Don't add a additional mass if it is zero in total
def test_set_load_division_zero():
    result = r.set_load(load_mass=-0.2, load_cog_x=0.02, load_cog_y=0.03, load_cog_z=0.04)
    robotiq_params = [element for element in r.get_tools() if element["name"] == "RobotiQ"][0]

    assert result and result[0]==0.0 
    assert result[7]==(robotiq_params['autoMeasureX'])
    assert result[8]==(robotiq_params['autoMeasureY'])
    assert result[9]==(robotiq_params['autoMeasureZ'])
