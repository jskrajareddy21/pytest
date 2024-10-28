# Learning points
'''
file name and function name should start with 'test'
run each functions individual ctrl+shift+f10
'''
import pytest
@pytest.mark.skip
def test_login():
    print("Login Successful")
@pytest.mark.sanity
def test_logoff():
    print("Log off successful")

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