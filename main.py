from imports import *

# The classes and methods format creates indented calculations which
# can be read easily by a computer through line inputs.ArithmeticError(
# 
# Examples of these "line inputs" can be seen below.

# Prints (1.0)
print(Product([
      Integer(2),
      Squareroot(
            Fraction(Integer(1), Integer(4))
      )
]).value)

# Prints 1.0
print(Product([
      Fraction(
            Integer(1),
            Integer(2)
      ),
      Fraction(
            Squareroot(Integer(4)),
            Fraction(
                  Integer(1),
                  Integer(2)
            )
      ),
      Fraction(
            Integer(1),
            Integer(2)
      )
]).value)