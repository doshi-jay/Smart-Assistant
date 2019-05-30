import math
import re

class Calculator:
	
	# Based on the operator, calls the corresponding 
	# operation
	def arithmetic_functions(self, operand1, operand2, operator):
		if operator == '+':
			return self.add(operand1, operand2)
		elif operator == '-':
			return self.subtract(operand1, operand2)
		elif operator == '*':
			return self.multiply(operand1, operand2)
		elif operator == '/':
			return self.divide(operand1, operand2)
		elif operator == 'mod':
			return self.modulus(operand1, operand2)
		elif operator == '**':
			return self.power(operand1, operand2)
		elif operator == '%':
			print ('perce')
			return self.percentage(operand1, operand2)

	def trigonometric_functions(self, expression):
		if (re.search("sin", expression)):
			return self.sine(int(expression.replace("sin", "").strip()))
		elif (re.search("cos", expression)):
			return self.cosine(int(expression.replace("cos", "").strip()))
		elif (re.search("tan", expression)):
			return self.tan(int(expression.replace("tan", "").strip()))
		elif (re.search("cosec", expression)):
			return self.cosecant(int(expression.replace("cosec", "").strip()))
		elif (re.search("sec", expression)):
			return self.secant(int(expression.replace("sec", "").strip()))
		elif (re.search("cot", expression)):
			return self.cot(int(expression.replace("cot", "").strip()))

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

	def percentage(self, percent, whole):
		 return (percent*whole)/100

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

	def cot(self, operand):
		return (1/self.tan(operand))
