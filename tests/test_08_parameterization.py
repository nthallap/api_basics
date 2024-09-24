import math
import pytest
from common_library.utils import get_test_data

@pytest.mark.parametrize("val", [10, 15, 16, 35, 1, 65])
def test_param1(val):
    assert val > 5, "value is not greater than 5"


@pytest.mark.para
@pytest.mark.parametrize("a, b", [(1, 2), (3, 5), (11, 6)])
def test_param2(a, b):
    assert a < b, "a is not less than b"


data = [
    ([1, 2, 3], "sum", 6),
    ([3, 5, 7], "mul", 105)
]


@pytest.mark.parametrize("li, oper, op", data)
def test_param3(li, oper, op):
    if oper == "sum":
        assert sum(li) == op
    elif oper == "mul":
        assert math.prod(li) == op


@pytest.mark.parametrize('a,b,c', get_test_data())
def test_read_csv(a, b, c):
    assert a
    assert b
    assert c

