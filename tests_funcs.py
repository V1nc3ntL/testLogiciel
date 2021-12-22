import funcs
import unittest

class TestFuncs(unittest.TestCase):

	def test_min(self):
		self.assertEqual(funcs.minimum_int([10, 15, 5, 20, 16]), 5)
		self.assertEqual(funcs.minimum_int([3, 15, 5, 20, 16]), 3)
		self.assertEqual(funcs.minimum_int([10, 15, 5, 20, 2]), 2)
		self.assertEqual(funcs.minimum_int([10, 15, 5, -20, 16]), -20)
		self.assertEqual(funcs.minimum_int([]), 0)

	def test_moyenne(self):
		self.assertEqual(funcs.moyenne([10, 15, 5, 20, 35]), 17)
		self.assertEqual(funcs.moyenne([10, 15, 5, 20, 16]), 13.2)
		self.assertEqual(funcs.moyenne([10, 15, 5, 20, 2]), 10.4)
		self.assertEqual(funcs.moyenne([10, 15, 5, -20, 16]), 5.2)
		self.assertEqual(funcs.moyenne([]), 0)


	def test_medianne(self):
		self.assertEqual(funcs.medianne([3, 1, 2]), 2)
		self.assertEqual(funcs.medianne([5]), 5)
		self.assertEqual(funcs.medianne([1,4,3,2]), 2.5)
		self.assertEqual(funcs.medianne([]), 0)
if __name__ == '__main__':
	unittest.main()