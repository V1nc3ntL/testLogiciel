#!/usr/bin/python3
import funcs
import unittest

class TestFuncs(unittest.TestCase):

	def test_connection(self):
		self.assertEqual(funcs.connect(),True)


if __name__ == '__main__':
	unittest.main()