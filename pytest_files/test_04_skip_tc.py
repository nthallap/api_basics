import sys

import pytest

#to skip whole suite
pytestmark = pytest.mark.skipif(sys.platform == "win32", reason="only running on linux")

@pytest.mark.skip(reason="not a valid tc")
def test_add():
    assert 2 + 2 == 4, "asserting addition"

def test_sub():
    assert 2 - 3 == -1, "asserting subtraction"

@pytest.mark.skipif(sys.version_info < (4, 8), reason="less python version")
def test_mul():
    assert 2 * 2 == 4, "multiplication failure "
