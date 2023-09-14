import unittest

from utils import utils

class test_numbers(unittest.TestCase):
	
	def test_reversed(self):
		utils_instance = utils()
		output = utils_instance.reversed(1234)
		self.assertEqual(output, 4321)
	
	def test_reversed_float(self):
		utils_instance = utils()
		output = utils_instance.reversed(2.3)
		self.assertEqual(output, "Type error")

	def test_reversed_string(self):
		utils_instance = utils()
		output = utils_instance.reversed('hello')
		self.assertEqual(output, "Type error")

	def test_formatter(self):
		utils_instance = utils()
		output = utils_instance.formatter(2341)
		self.assertEqual(output, ('0b100100100101', '0o4445'))

	def test_formatter_float(self):
		utils_instance = utils()
		output = utils_instance.reversed(2.3)
		self.assertEqual(output, "Type error")

	def test_formatter_string(self):
		utils_instance = utils()
		output = utils_instance.reversed('hello')
		self.assertEqual(output, "Type error")


if __name__ == '__main__':
    unittest.main()