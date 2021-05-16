from imports import *

# The classes and methods format creates indented calculations which
# can be read easily by a computer through line input
# 
# Examples of these "line inputs" can be seen below.

# Prints 1.0
print(RoundValue(
      Product([
            Squareroot(Integer(98)),
            Fraction(
                  Integer(1),
                  Squareroot(Integer(2))
            ),
            Fraction(
                  Integer(1),
                  Integer(7)
            )
      ]).value
))