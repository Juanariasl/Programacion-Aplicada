# clase.py
import random

class Square:
   def __init__(self, val):
      self.val = val
   
   def getVal(self):
      return self.val * self.val


class Add_Sub:
   def add(self, a, b):
      return a + b
   
   def sub(self, a, b):
      return a - b


class Mul_Div:
   def mul(self, a, b):
      return a * b
   
   def div(self, a, b):
      if b != 0:
         return a / b
      else:
         return "Cannot divide by zero"


class RandomCalculator:
   def __init__(self):
      self.square = Square(random.randint(1, 10))  # Valor aleatorio entre 1 y 10
      self.add_sub = Add_Sub()
      self.mul_div = Mul_Div()

   def calculate(self):
      a = random.randint(1, 10)  # Primer número aleatorio
      b = random.randint(1, 10)  # Segundo número aleatorio

      # Elegir operación aleatoriamente
      operation = random.choice(['add', 'sub', 'mul', 'div', 'square'])
      
      if operation == 'add':
         result = self.add_sub.add(a, b)
         return f"Addition of {a} and {b}: {result}"
      
      elif operation == 'sub':
         result = self.add_sub.sub(a, b)
         return f"Subtraction of {a} and {b}: {result}"
      
      elif operation == 'mul':
         result = self.mul_div.mul(a, b)
         return f"Multiplication of {a} and {b}: {result}"
      
      elif operation == 'div':
         result = self.mul_div.div(a, b)
         return f"Division of {a} by {b}: {result}"
      
      elif operation == 'square':
         val = random.randint(1, 10)
         square_instance = Square(val)
         result = square_instance.getVal()
         return f"Square of {val}: {result}"
