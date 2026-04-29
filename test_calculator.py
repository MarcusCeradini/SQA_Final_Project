import pytest
from calculator import Calculator
@pytest.fixture
def calc():
    return Calculator()

class TestAdd:

    def test_positive_overflow(self, calc):
        with pytest.raises(OverflowError):
            calc.divide(1, 9223372036854775807)

class TestSubtract:


class TestMultiply:


class TestDivide:

    def test_even_division(self, calc):
        assert calc.divide(10, 2) == pytest.approx(5.0)

    def test_zero_divisor_raises(self, calc):
        with pytest.raises(ZeroDivisionError):
            calc.divide(5, 0)


class TestPower:


class TestSquareRoot:


class TestModulus:


class TestFloorDivide:
