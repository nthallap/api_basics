import pytest
import sys


@pytest.mark.xfail(reason="known issue")
def test_div():
    assert 2 / 2 == 0, "multiplication failure "

@pytest.mark.xfail(sys.platform == "win32", reason="fails only on linux")
def test_upper():
    assert "naga".upper() == "NAGA"

@pytest.mark.xfail(raises=TypeError, reason="type error comes")
def test_lower():
    assert "NAGA" + 5 == 55
