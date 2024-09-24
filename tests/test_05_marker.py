import pytest

pytestmark = [pytest.mark.smoke, pytest.mark.stress]

class TestMyStr:
    @pytest.mark.sanity
    @pytest.mark.str
    def test_upper(self):
        assert "naga".upper() == "NAGA"

    @pytest.mark.sanity
    @pytest.mark.str
    def test_lower(self):
        assert  "NAGA".lower() == "naga"

    @pytest.mark.sanity
    @pytest.mark.str
    def test_slicing(self):
        assert "NAGA"[1] == "A"

    @pytest.mark.sanity
    @pytest.mark.math
    def test_add(self):
        assert 2 + 2 == 4, "asserting addition"

    @pytest.mark.sanity
    @pytest.mark.math
    def test_sub(self):
        assert 2 - 3 == -1, "asserting subtraction"

    @pytest.mark.sanity
    @pytest.mark.math
    def test_mul(self):
        assert 2 * 2 == 4, "multiplication failure "

    #to specify the failure of test
    @pytest.mark.xfail(reason="known issue")
    def test_div(self):
        assert 2 / 2 == 0, "multiplication failure "