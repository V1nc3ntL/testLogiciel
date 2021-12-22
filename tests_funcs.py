import funcs
import unittest

class TestFuncs(unittest.TestCase):

	def test_min(self):
		self.assertEqual(funcs.minimum_int([10, 15, 5, 20, 16], 5)
		self.assertEqual(funcs.minimum_int([3, 15, 5, 20, 16], 3)
		self.assertEqual(funcs.minimum_int([10, 15, 5, 20, 2], 2)
		self.assertEqual(funcs.minimum_int([10, 15, 5, -20, 16], -20)

if __name__ == '__main__':
	unittest.main()