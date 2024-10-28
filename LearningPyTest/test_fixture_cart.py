import pytest

@pytest.fixture
def setUp():
    print()
    print("Launch browser")
    print("Login")
    yield
    print("Log off")


def test_AddItemtoCart(setUp):
    print()
    print("added item Successful")
    print("added another item successful")

def test_RemoveItemtoCart():
    print("Remove Item Successful")

#Output
'''
============================= test session starts =============================
collecting ... collected 2 items

test_fixture_cart.py::test_AddItemtoCart 
Launch browser
Login
PASSED                                  [ 50%]
added item Successful
added another item successful
Log off

test_fixture_cart.py::test_RemoveItemtoCart PASSED                               [100%]Remove Item Successful


============================== 2 passed in 0.02s ==============================
'''