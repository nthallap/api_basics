import pytest
import sys


@pytest.mark.xfail(reason="known issue")
def test_div():
    assert 2 / 2 == 0, "multiplication failure "


# this test case is failing intentionally
@pytest.mark.xfail(sys.platform == "linux", reason="xfail only on linux failed tc on windows")
def test_upper():
    assert "naga".upper() == "RAMA"


@pytest.mark.xfail(raises=TypeError, reason="type error comes")
def test_lower():
    assert "NAGA" + 5
