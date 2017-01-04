import sys

class InputCheck(object):

	inputValue = ""

	def __init__(self, value):
		self.inputValue = value
		pass
		

	def input_scan(self,inputList):
		try:
			if self.inputValue == "":
				raise SyntaxError
		except SyntaxError:
			print "Error: Empty input"
		except ValueError:
			print "Enter String only"
		else: 
			if len(self.inputValue) == 1 and self.inputValue not in inputList:
				inputList.append(self.inputValue)
		return self.inputValue




