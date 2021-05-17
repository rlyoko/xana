from fractions import gcd as s__Gcd

class Floor:
      def __init__(self, num):
            self.num = num
            self.value = int(num.value)

class Ceiling:
      def __init__(self, num):
            self.num = num
            self.value = int(float(num.value) - 0.0000000001) + 1

class Gcd:
      def __init__(self, a, b):
            self.a = a
            self.b = b
            self.value = s__Gcd(a, b)

class Lcm:
      def __init__(self, a, b):
            self.a = a
            self.b = b
            self.value = a*b/s__Gcd(a,b)