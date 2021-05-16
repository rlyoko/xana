class Product:
      def __init__(self, x):
            self.factors = x
            
            self.value = 1
            for num in self.factors:
                  self.value *= num.value

class Sum:
      def __init__(self, x):
            self.addends = x

            self.value = 0
            for addend in self.addends:
                  self.value += addend.value

class Subtract:
      def __init__(self, x):
            self.subtrahends = x
            self.value = x[0].value - x[1].value

class Divide:
      def __init__(self, x):
            self.dividends = x
            self.value = x[0]/x[1]

class Squareroot:
      def __init__(self, num):
            self.num = num
            self.value = num.value ** 0.5

class Nthroot:
      def __init__(self, n, num):
            self.index = n
            self.num = num
            self.value = num.value ** float(1/n.value)