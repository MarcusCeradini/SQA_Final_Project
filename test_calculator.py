import pytest
from calculator import calculator
@pytest.fixture
def calc():
    return calculator()

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
        Calculator.add(0.5,0.5) == pytest.approx(1.0)

    def test_adding_negative_and_positive_decimals(self, calc):
        Calculator.add(-0.5, 0.5) == pytest.approx(0.0)
    

#class TestSubtract:


#class TestMultiply:

    def test_multiplying_positive_by_negative(self, calc):
        assert Calculator.multiply(10, -90) == -900

class TestDivide:

    def test_even_division(self, calc):
        assert calculator.divide(10, 2) == pytest.approx(5.0)

    def test_raises_zero_division(self,calc):
        with pytest.raises(ZeroDivisionError):
            assert calculator.divide(5,0)

    def test_max_boundary(self,calc):
        with pytest.raises(OverflowError):
            calculator.divide(1e250, 0.2)

    def test_min_boundary(self,calc):
        with pytest.raises(OverflowError):
            calculator.divide(-1e250, 0.2)
    
    def test_negative_division(self,calc):
        assert calculator.divide(-5.5, -10) == pytest.approx(0.55)

    def test_negative_numerator(self,calc):
        assert calculator.divide(-5,10) == pytest.approx(-0.5)


class TestPower:
    def test_positive_integers(self,calc):
        assert calculator.power(2,2) == 4

    def test_max_boundary(self,calc):
        with pytest.raises(OverflowError):
            calculator.power(1e550, 2)

    def test_min_boundary(self,calc):
        with pytest.raises(OverflowError):
            calculator.power(-1e560, 7)

    def test_under_positive_boundary(self,calc):
        assert calculator.power(1e+125 - 1,2) == pytest.approx(1e250 - 1)

    def test_under_negative_boundary(self,calc):
        assert calculator.power(-1e+125 + 1,2) == pytest.approx(1e250 - 1)

    

    def test_value_error(self,calc):
        with pytest.raises(ValueError):
            calculator.power(5, -2)

    

class TestSquareRoot:
    def test_float_square_root(self,calc):
        assert calculator.square_root(25.0) == pytest.approx(5.0)

    def test_zero_square(self,calc):
        assert calculator.square_root(0) == pytest.approx(0.0)

    def test_integer_square_root(self,calc):
        assert calculator.square_root(25) == 5

    def test_raises_value_error(self,calc):
        with pytest.raises(ValueError):
            calculator.square_root(-25)


class TestModulus:
    def test_raises_zero_divisoon(self,calc):
        with pytest.raises(ZeroDivisionError):
            assert calculator.modulus(5,0)

    def test_modulus_boundary(self,calc):
        assert calculator.modulus(9223372036854,4) == 2

    def test_modulus_float(self,calc):
        assert calculator.modulus(5.0,5) == pytest.approx(0.0)


class TestFloorDivide:
    def test_raises_zero_division(self,calc):
        with pytest.raises(ZeroDivisionError):
            assert calculator.floor_divide(5,0)

    def test_floor_dividing_boundary(self,calc):
        assert calculator.floor_divide(9223372036854775807,30.0) == pytest.approx(3.0744573e+17)

    def test_int_floor_division(self,calc):
        assert calculator.floor_divide(30,5) == 6


class TestChain:
    def test_chaining_ops(self,calc):
        assert calculator.subtract(calculator.add(calculator.divide(calculator.multiply(5,5),10),5),3) == pytest.approx(4.5)