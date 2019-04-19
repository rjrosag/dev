import unittest
import calc

class TestCalc( unittest.testCase):

	def test_add(self):
		result = calc.add(10, 5)
		self.assertEqual(result, 15)

if __name__ == "__main__":
	unittest.mani()
