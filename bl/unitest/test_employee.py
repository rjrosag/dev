import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):

	def setUp(self):
		self.emp1 = Employee('Cory', 'Schafer', 6000)
		self.emp2 = Employee('Sam', 'Smith', 5000)
	def tearDown(self):
		pass
	@classmethod


	def setUpClass(cls):

		print('Class setup')
	@classmethod
	def tearDown(cls):
		print('Class tear down')



