class Integer:
      def __init__(self, value):
            self.value = value

class Fraction:
      def __init__(self, numerator, denominator):
            self.numerator = numerator
            self.denominator = denominator

            self.value = numerator.value/denominator.value

class Rational:
      def __init__(self, value):
            self.value = value
                  

class Product:
      def __init__(self, values):
            self.factors = values

            self.value = 1
            for factor in self.factors:
                  self.value *= factor.value

class Squareroot:
      def __init__(self, radicand):
            self.radicand = radicand

            self.value = radicand.value ** 0.5

class Nthroot:
      def __init__(self, index, radicand):
            self.index = index
            self.radicand = radicand
            
            self.value = radicand.value ** float(1/self.index.value)
