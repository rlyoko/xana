def RoundInt(k):
      if (abs(k.value%1 - 1) < 0.000001 or abs(k.value%1) < 0.000001 or abs(k.value%1) == 0):
            k.value = int(k.value + 0.01)
      return k