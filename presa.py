try:
    class Calculator:
        @classmethod
        def plus(cls, a, b):
            return a+b

        @classmethod
        def minus(cls, a, b):
            return a - b

        @classmethod
        def multiplication(cls, a, b):
            return a * b

        @classmethod
        def division(cls, a, b):
            return a / b

        @classmethod
        def exponent(cls, a, b):
            return a**b

        @classmethod
        def root(cls, a, b):
            return pow(a, 1/b)


    print(Calculator.root('a', 2))
except TypeError as e:
    print(f'Enter int or float. Error: {e}')



