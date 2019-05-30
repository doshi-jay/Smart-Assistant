import calculator
import re

CALCULATE = "calculate"

class Controller:

	def interface(self, input_):
		if input_.startswith(CALCULATE):
			return self.calculate(input_.replace(CALCULATE), "")
		return input_

	def calculate(self, input_):
		expression = input_.strip()
		if (re.search("(.*[\+].*)|(.*[-].*)|(.*[\*].*)|(.*[\/].*)|(.*[%].*)", expression)):
			operand1 = list(expression)[0]
			operator = list(expression)[1]
			operand2 = list(expression)[2]
			return calculator.calculate(operand1, operand2, operator)
	