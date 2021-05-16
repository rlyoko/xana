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
      def __init__(self, x):
            try:
                  self.value = x.value
            except:
                  self.value = x

            self.fraction = Fraction(
                  Integer(int(stringToFraction(str(self.value)).numerator)),
                  Integer(int(stringToFraction(str(self.value)).denominator))
            )