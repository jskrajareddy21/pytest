import pytest
'''
it works like a loop
a,b,final values are passing one by one to the function
'''
@pytest.mark.parametrize("a,b,final",[(2,6,8), (5,8,13), (5,10,15)])
def testAdd(a,b,final):
    assert a+b == final