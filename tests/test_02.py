import math


class TestMyMath:

    def test_sqrt(self):
        assert math.sqrt(10) > 3, "asserting sqrt of 4"

    def test_power(self):
        assert math.pow(5, 4) > 600, "5 power 4 asserting"
