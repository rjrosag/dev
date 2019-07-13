class Calc:

	def add(num1, num2):
		return(num1+num2)

	def divide(num1, num2):
		if num2 == 0: 

			raise VallueError("Error: cannot devide by zero")

		return(num1 / num2)

