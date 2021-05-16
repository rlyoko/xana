from imports import *

print(
      Sum([
            Product([
                  Fraction(
                        Integer(1),
                        Integer(2)
                  ),
                  Fraction(
                        Integer(3),
                        Integer(4)
                  )
            ]),
            Fraction(
                  Integer(7),
                  Integer(4)
            ),
            Nthroot(
                  Integer(3),
                  Decimal(0.125)
            )
      ]).value
)