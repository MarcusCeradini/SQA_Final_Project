import pytest
from Calculator import Calculator
@pytest.fixture
def calc():
    return Calculator()

class TestAdd:

    def test_positive_overflow(self, calc):
        with pytest.raises(OverflowError):
            Calculator.add(1.0, 1e250**2)

    def test_adding_positives_wholes(self, calc):
        assert Calculator.add(3, 10) == 13

    def test_adding_two_negatives(self, calc):
        assert Calculator.add(-5, -8) == -13

    def test_adding_negative_and_positive(self, calc):
        assert Calculator.add(-5.0, 8.0) == 3.0

    def test_negative_overflow(self, calc):
        with pytest.raises(OverflowError):
            Calculator.add(-1.0, -1e250**2)
    
    def test_positive_boundary(self, calc):
        Calculator.add(1e250, -1) == 1e250 - 1

    def test_negative_bounday(self, calc):
        Calculator.add(-1e250, 1) == -1e250 + 1

    def test_adding_decimals(self, calc):
        Calculator.add(0.5,0.5) == 1.0

    def test_adding_negative_and_positive_decimals(self, calc):
        Calculator.add(-0.5, 0.5) == 0
    

#class TestSubtract:


class TestMultiply:

    def test_multiplying_positive_by_negative(self, calc):
        assert Calculator.multiply(10, -90) == -900

#class TestDivide:

    # def test_even_division(self, calc):
    #     assert calc.divide(10, 2) == pytest.approx(5.0)

    # def test_zero_divisor_raises(self, calc):
    #     with pytest.raises(ZeroDivisionError):
    #         calc.divide(5, 0)


#class TestPower:


#class TestSquareRoot:


#class TestModulus:


#class TestFloorDivide: