import pytest
from Calculator import Calculator
@pytest.fixture
def calc():
    return Calculator()

#class TestAdd:

#class TestSubtract:


#class TestMultiply:


#class TestDivide:

#    def test_even_division(self, calc):
#        assert calc.divide(10, 2) == pytest.approx(5.0)

#    def test_zero_divisor_raises(self, calc):
#        with pytest.raises(ZeroDivisionError):
#            calc.divide(5, 0)


#class TestPower:


class TestSquareRoot:
    def test_float_square_root(self,calc):
        assert Calculator.square_root(25.0) == 5.0

    def test_zero_square(self,calc):
        assert Calculator.square_root(0) == 0.0

    def test_integer_square_root(self,calc):
        assert Calculator.square_root(25) == 5

    def test_raises_value_error(self,calc):
        with pytest.raises(ValueError):
            Calculator.square_root(-25)


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

    def test_floor_dividing_boundary(self,calc):
        assert Calculator.floor_divide(9223372036854775807,30.0) == pytest.approx(3.0744573e+17)

    def test_int_floor_division(self,calc):
        assert Calculator.floor_divide(30,5) == 6


class TestChain:
    def test_chaining_ops(self,calc):
        assert Calculator.subtract(Calculator.add(Calculator.divide(Calculator.multiply(5,5),10),5),3) == 4.5