
class utils:	
	def reversed(self, number):
		reversedNum = 0

		#check for type
		if not (isinstance(number, int)):
			return("Type error")


		while (number != 0):
			reversedNum = reversedNum * 10 + number%10
			number = number//10
		return reversedNum


	def formatter(self, number):
		#check for type
		if not (isinstance(number, int)):
			return("Type error")

		baseTwo = bin(number)
		baseEight = oct(number)
		return baseTwo, baseEight
