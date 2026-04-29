import pytest
from Calculator import Calculator
@pytest.fixture
def calc():
    return Calculator()

#class TestAdd:

   # def test_positive_overflow(self, calc):
        #with pytest.raises(OverflowError):
       #     calc.divide(1, 9223372036854775807)

#class TestSubtract:


#class TestMultiply:


#class TestDivide:

#    def test_even_division(self, calc):
#        assert calc.divide(10, 2) == pytest.approx(5.0)

#    def test_zero_divisor_raises(self, calc):
#        with pytest.raises(ZeroDivisionError):
#            calc.divide(5, 0)


#class TestPower:


#class TestSquareRoot:


#class TestModulus:


class TestFloorDivide:
    def test_raises_zero_division(self,calc):
        with pytest.raises(ZeroDivisionError):
           Calculator.floor_divide(5,0)

    def test_dividing_boundary(self,calc):
        assert Calculator.floor_divide(9223372036854775807,30.0) == pytest.approx(3.0744573e+17)

    def test_floor_division(self,calc):
        assert Calculator.floor_divide(30,5) == 6