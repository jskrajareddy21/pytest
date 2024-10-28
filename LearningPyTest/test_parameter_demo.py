'''

'''
import pytest
@pytest.fixture(params=["a","b"])
def demo_fixture(request):
    print(request.param)

def test_login(demo_fixture):
    print()
    print("Login Successful")
# @pytest.mark.sanity
# def test_logoff():
#     print("Log off successful")
#
# def test_calculation():
#     assert 2+2 == 4