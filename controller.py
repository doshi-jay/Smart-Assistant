from calculator import Calculator
import re


class Controller:

	def interface(self, input_):
		if input_.startswith("calculate"):
			return self.calculate(input_.replace("calculate", ""))
		return input_

	def calculate(self, input_):
		calculator = Calculator()
		expression = input_.strip()
		
		if (re.search("(.*[\+\-\*\/%].*)", expression) or re.search("mod", expression)):
			exp = expression.split(" ")
			operand1 = exp[0]
			operator = exp[1]
			operand2 = exp[2]
			return calculator.arithmetic_functions(float(operand1), float(operand2), operator)
		
		elif (re.search("(sin\(\d\))|([cos\(\d\)])|(tan\(\d\))|(sec\(\d\))|(cosec\(\d\))|(cot\(\d\))", expression)):
			expression = expression.replace("(", " ")
			expression = expression.replace(")", " ")
			expression = expression.strip()
			return calculator.trigonometric_functions(expression)
	