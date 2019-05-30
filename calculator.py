import math

class calculator:
	
	# Based on the operator, calls the corresponding 
	# operation
	def calculate(self, operand1, operand2, operator):
		if operator == '+':
			return self.add(operand1, operand2)
		elif operator == '-':
			return self.subtract(operand1, operand2)
		elif operator == '*':
			return self.multiply(operand1, operand2)
		elif operator == '/':
			return self.divide(operand1, operand2)
		elif operator == '%':
			return self.modulus(operand1, operand2)
		elif operator == '**':
			return self.power(operand1, operand2)

	def add(self, operand1, operand2):
		return operand1 + operand2

	def subtract(self, operand1, operand2):
		return operand1 - operand2

	def multiply(self, operand1, operand2):
		return operand1 * operand2

	def divide(self, operand1, operand2):
		if operand2 == 0:
			print ("Divide by zero error")
			return
		return operand1 / operand2

	def modulus(self, operand1, operand2):
		return operand1 % operand2

	def power(self, base, power):
		return base**power

	def sine(self, operand):
		return math.sin(operand)

	def cosine(self, operand):
		return math.cos(operand)

	def tan(self, operand):
		return math.tan(operand)

	def secant(self, operand):
		return (1/self.cosine(operand))

	def cosecant(self, operand):
		return (1/self.sine(operand))

	def cotan(self, operand):
		return (1/self.tan(operand))

	def percentage(self, percent, whole):
		 return (percent*whole)/100