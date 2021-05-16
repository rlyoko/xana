from imports import *

# The classes and methods format creates indented calculations which
# can be read easily by a computer through line input
# 
# Examples of these "line inputs" can be seen below.

# Prints 1.0
print(RoundValue(
      Subtract([
            Integer(1),
            Sum([
                  Fraction(
                        Integer(1),
                        Integer(2)
                  ),
                  Fraction(
                        Integer(1),
                        Integer(4)
                  )
            ])
      ]).value
))