#Working
import os
SOCKET_INTERFACE = os.getenv('SOCKET_INTERFACE',"false").lower()=='true'
if SOCKET_INTERFACE:
    from neurapy.socket_interface.robot import Robot
else:
    from neurapy.robot import Robot
import random
import string
import pytest

r = Robot()

def test_get_point():
    result = r.get_point("Home")
    assert result is "True" or "False"

@pytest.mark.skipif(Robot().robot_name == 'maira7M',reason="Current robot is not lara")
def test_save_point():
    point_name = "".join(random.choices(string.ascii_letters, k=7))
    point_coordinates = [0, -0.347247, 0.139187, 3.1416, -0.6458, -1.5708]
    (x, y, z, a, b, c) = point_coordinates
    point_joints = [1.5708001839725434, 0, -2.49582083, 0, 0, 0]
    (a1, a2, a3, a4, a5, a6) = point_joints
    point_data = {
        "type": "Point",
        "visibility": True,
        "description": "Description of your point",
        "originX": x,
        "originY": y,
        "originZ": z,
        "originA": a,
        "originB": b,
        "originC": c,
        "offsetX": 0,
        "offsetY": 0,
        "offsetZ": 0,
        "offsetA": 0,
        "offsetB": 0,
        "offsetC": 0,
        "a1": a1,
        "a2": a2,
        "a3": a3,
        "a4": a4,
        "a5": a5,
        "a6": a6,
        "name": point_name,
        "__v": 0
    }
    result = r.save_point(point_data)
    assert result is True
    assert r.get_point(point_name) == point_joints
    assert r.get_point(point_name, representation="Cartesian") == point_coordinates

@pytest.mark.skipif(Robot().robot_name != 'maira7M',reason="Current robot is not maira7M")
def test_save_point_maira():
    point_name = "".join(random.choices(string.ascii_letters, k=7))
    point_coordinates = [0, -0.347247, 0.139187, 3.1416, -0.6458, -1.5708]
    (x, y, z, a, b, c) = point_coordinates
    point_joints = [1.5708001839725434, 0, -2.49582083, 0, 0, 0,0]
    (a1, a2, a3, a4, a5, a6,a7) = point_joints
    point_data = {
        "type": "Point",
        "visibility": True,
        "description": "Description of your point",
        "originX": x,
        "originY": y,
        "originZ": z,
        "originA": a,
        "originB": b,
        "originC": c,
        "offsetX": 0,
        "offsetY": 0,
        "offsetZ": 0,
        "offsetA": 0,
        "offsetB": 0,
        "offsetC": 0,
        "a1": a1,
        "a2": a2,
        "a3": a3,
        "a4": a4,
        "a5": a5,
        "a6": a6,
        "a7": a7,
        "name": point_name,
        "__v": 0
    }
    result = r.save_point(point_data)
    assert result is True
    assert r.get_point(point_name) == point_joints
    assert r.get_point(point_name, representation="Cartesian") == point_coordinates