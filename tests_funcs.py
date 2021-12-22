import funcs
import unittest

class TestFuncs(unittest.TestCase):

	def test_min(self):
		self.assertEqual(funcs.max_int(0,2),2)
		self.assertEqual(funcs.max_int(-1,-5),-1)
		self.assertEqual(funcs.max_int(-1,2),2)
		self.assertEqual(funcs.max_int(0,0),0)

if __name__ == '__main__':
	unittest.main()