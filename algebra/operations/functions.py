def roundValue(x):
      if (abs(x%1 - 1) < 0.000001):
            return int(x+0.1)
      else:
            return x
