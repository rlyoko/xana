class Product:
      def __init__(self, x):
            self.factors = x
            
            self.value = 1
            for num in self.factors:
                  self.value *= num.value