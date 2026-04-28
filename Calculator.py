import math as math

class Calculator:
    #max_value = 9223372036854775807.0
    #min_value = -9223372036854775808.0
    
    def add(a, b):
        max_value = 9223372036854775807.0
        min_value = -9223372036854775808.0

        if a + b > max_value:
            raise OverflowError
        
        if (a + b) < min_value:
            raise OverflowError
        
        return float(a + b)
    
    def subtract(a, b):
        max_value = 9223372036854775807.0
        min_value = -9223372036854775808.0

        if (a - b) > max_value:
            raise OverflowError
        
        if (a - b) < min_value:
            raise OverflowError
        return float(a - b)
    
    def multiply(a, b):
        max_value = 9223372036854775807.0
        min_value = -9223372036854775808.0

        if (a * b) > max_value:
            raise OverflowError
        
        if (a * b) < min_value:
            raise OverflowError
        return float(a * b)
    
    def divide(a, b):
        max_value = 9223372036854775807.0
        min_value = -9223372036854775808.0

        if (a / b) > max_value:
            raise OverflowError
        
        if (a / b) < min_value:
            raise OverflowError

        if b == 0:
            raise ZeroDivisionError
        return float(a / b)
    
    def power(base, exp):
        max_value = 9223372036854775807.0
        min_value = -9223372036854775808.0

        if math.pow(base, exp) > max_value:
            raise OverflowError
        
        if math.pow(base, exp) < min_value:
            raise OverflowError

        if base and exp == 0:
            raise ValueError
        return float(math.pow(base, exp))
    
    def square_root(a):
        if a < 0:
            raise ValueError
        return float(math.sqrt(a))
    
    def modulus(a, b):
        if b == 0:
            raise ZeroDivisionError
        return float(a % b)
    
    def floor_divide(a, b):
        if b == 0:
            raise ZeroDivisionError
        return float(math.floor(a / b))
    
Calculator.add(10.0, 29.0)
Calculator.subtract(10.0, 29.0)
Calculator.multiply(10.0, 29.0)
Calculator.divide(10.0, 29.0)
Calculator.power(10.0, 2.0)
Calculator.square_root(10.0)
Calculator.modulus(10.0, 29.0)
Calculator.floor_divide(10.0, 29.0)