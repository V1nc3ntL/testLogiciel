#!/usr/bin/python3
import funcs
import unittest
import sqlite3
import exdef

class TestFuncs(unittest.TestCase):

	def test_connection(self):
		self.assertTrue(funcs.connect()[0])


if __name__ == '__main__':
	unittest.main()