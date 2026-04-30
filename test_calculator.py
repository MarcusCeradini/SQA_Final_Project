import pytest
from Calculator import Calculator
@pytest.fixture
def calc():
    return Calculator()

#class TestAdd:

#class TestSubtract:


#class TestMultiply:


class TestDivide:

    def test_even_division(self, calc):
        assert Calculator.divide(10, 2) == pytest.approx(5.0)

    def test_zero_division_error(self, calc):
        with pytest.raises(ZeroDivisionError):
            Calculator.divide(0, 0)

    def test_max_boundary(self,calc):
        with pytest.raises(OverflowError):
            Calculator.divide(1e250, 0.2)

    def test_min_boundary(self,calc):
        with pytest.raises(OverflowError):
            Calculator.divide(-1e250, 0.2)
    
    def test_negative_division(self,calc):
        assert Calculator.divide(-5.5, -10) == pytest.approx(0.55)

    def test_negative_numerator(self,calc):
        assert Calculator.divide(-5,10) == pytest.approx(-0.5)


class TestPower:
    def test_positive_integers(self,calc):
        assert Calculator.power(2,2) == 4

    def test_under_positive_boundary(self,calc):
        assert Calculator.power(1e+125 - 1,2) == pytest.approx(1e250 - 1)

    def test_under_negative_boundary(self,calc):
        assert Calculator.power(-1e+125 + 1,2) == pytest.approx(1e250 - 1)

    def test_max_boundary(self,calc):
        with pytest.raises(OverflowError):
            Calculator.power(1e250, 2)

    def test_min_boundary(self,calc):
        with pytest.raises(OverflowError):
            Calculator.power(-1e250, 2)

    def test_value_error(self,calc):
        with pytest.raises(ValueError):
            Calculator.power(0, -9)

    

class TestSquareRoot:
    def test_float_square_root(self,calc):
        assert Calculator.square_root(25.0) == pytest.approx(5.0)

    def test_zero_square(self,calc):
        assert Calculator.square_root(0) == pytest.approx(0.0)

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
        assert Calculator.modulus(5.0,5) == pytest.approx(0.0)


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
        assert Calculator.subtract(Calculator.add(Calculator.divide(Calculator.multiply(5,5),10),5),3) == pytest.approx(4.5)