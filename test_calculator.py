import pytest
from Calculator import Calculator
@pytest.fixture
def calc():
    return Calculator()

class TestAdd:

    def test_positive_overflow(self, calc):
        with pytest.raises(OverflowError):
            calc.divide(1, 1e250)

    def test_adding_three_ten(self,calc):
        assert Calculator.add(3,10) == 13.0

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


class TestModulus:
    def test_raises_zero_divisoon(self,calc):
        with pytest.raises(ZeroDivisionError):
            assert Calculator.modulus(5,0)

    def test_modulus_boundary(self,calc):
        assert Calculator.modulus(9223372036854,4) == 2

    def test_modulus_float(self,calc):
        assert Calculator.modulus(5.0,5) == 0.0


class TestFloorDivide:
    def test_raises_zero_division(self,calc):
        with pytest.raises(ZeroDivisionError):
            assert Calculator.floor_divide(5,0)

    def test_dividing_boundary(self,calc):
        assert Calculator.floor_divide(9223372036854775807,30.0) == pytest.approx(3.0744573e+17)

    def test_floor_division(self,calc):
        assert Calculator.floor_divide(30,5) == 6

#Class TestChain:
    #def test_chaining_ops