class Integer:
      def __init__(self, value):
            self.value = value

class Fraction:
      def __init__(self, num, den):
            self.numerator = num
            self.denominator = den
            self.value = num.value/den.value

class Squareroot:
      def __init__(self, num):
            self.num = num
            self.value = num.value ** 0.5