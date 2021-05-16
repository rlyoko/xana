from fractions import Fraction as stringToFraction

class Integer:
      def __init__(self, value):
            self.value = value

class Decimal:
      def __init__(self, value):
            self.value = value
            self.numerator = Integer(int(
                  stringToFraction(str(value)).numerator
            ))
            self.denominator = Integer(int(
                  stringToFraction(str(value)).denominator
            ))

class Fraction:
      def __init__(self, num, den):
            self.numerator = num
            self.denominator = den
            self.value = num.value/den.value

class Squareroot:
      def __init__(self, num):
            self.num = num
            self.value = num.value ** 0.5

class Nthroot:
      def __init__(self, n, num):
            self.index = n
            self.num = num
            self.value = num.value ** float(1/n)