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
		
		if (re.search("(\d*\*{2}\d*)|(\d*mod\d*)", expression)):
			return calculator.arithmetic_functions(expression.replace(" ", ""))
		elif (re.search("(\d*[\+\-\*\/%]\d*)", expression) or re.search("mod", expression)):
			return calculator.arithmetic_functions(expression.replace(" ", ""))
		
		elif (re.search("(sin\(\d\))|([cos\(\d\)])|(tan\(\d\))|(sec\(\d\))|(cosec\(\d\))|(cot\(\d\))", expression)):
			expression = expression.replace("(", " ")
			expression = expression.replace(")", " ")
			expression = expression.strip()
			return calculator.trigonometric_functions(expression)
	