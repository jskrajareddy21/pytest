import pytest
'''
conftest is used to fixtures can used in all test files. example test_conftest_cart.py
'''
@pytest.fixture(autouse=True)
def setUp():
    print()
    print("Launch browser")
    print("Login")
    yield
    print("Log off")