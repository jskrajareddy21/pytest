# Learning points
'''
pytest.mark.<any reasonable name>, if you want to execute only marked function then use mark option
'''
import pytest


def test_login():
    print("Login Successful")

def test_logoff():
    print("Log off successful")

@pytest.mark.sanity
def test_calculation():
    assert 2+2 == 4

#Output
'''
============================= test session starts =============================
collecting ... collected 3 items

test_login.py::test_login PASSED               [ 33%]Login Successful

test_login.py::test_logoff PASSED              [ 66%]Log off successful

test_login.py::test_calculation PASSED         [100%]

============================== 3 passed in 0.03s ==============================
'''