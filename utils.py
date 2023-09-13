
class utils:	
	def reversed(number):
		reversedNum = 0

		while (number != 0):
			reversedNum = reversedNum * 10 + number%10
			number = number//10
		return reversedNum


	def formatter(number):
		baseTwo = bin(number)
		baseEight = oct(number)
		return baseTwo, baseEight
