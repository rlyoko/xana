from fractions import Fraction as stringToFraction

class Integer:
      def __init__(self, value):
            self.value = value

class Fraction:
      def __init__(self, num, den):
            self.value = num.value/den.value
            self.numerator = Integer(int(stringToFraction(str(self.value)).numerator))
            self.denominator = Integer(int(stringToFraction(str(self.value)).denominator))

class Decimal:
      def __init__(self, value):
            self.value = value
            self.numerator = Integer(int(stringToFraction(str(value)).numerator))
            self.denominator = Integer(int(stringToFraction(str(value)).denominator))
            self.fraction = Fraction(self.numerator, self.denominator)