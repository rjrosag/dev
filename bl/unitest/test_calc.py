import unittest
import calc

class TestCalc( unittest.testCase):

	def test_add(self):
		result = calc.add(10, 5)
		self.assertEqual(result, 15)




		
		self.assertEqual(calc.divide(10,5), 2)
		self.assertRaise(ValueError, calc.divide, 10,0)
		with self.assertRaises(ValueError):
			calc.divide(10,0)

				




if __name__ == "__main__":
	unittest.main()
