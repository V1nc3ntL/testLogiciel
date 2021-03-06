#!/usr/bin/python3
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

	def test_ecartType(self):
		self.assertEqual(funcs.ecartType([1,2,3,4,5]), 1.4142135623730951)
		self.assertEqual(funcs.ecartType([10,0,80,45,20, 60]), 28.345585586158247)
		self.assertEqual(funcs.ecartType([5,10,6,8,3,4]), 2.3804761428476167)
		self.assertEqual(funcs.ecartType([]), 0)

	def test_isGeometric(self):
		self.assertEqual(funcs.isGeometric([24,12,6,3]), True)
		self.assertEqual(funcs.isGeometric([1,2,4,8,16,32]), True)
		self.assertEqual(funcs.isGeometric([1,3,9,12,15]), False)
		self.assertEqual(funcs.isGeometric([1,16,9,14,3]), False)
		self.assertEqual(funcs.isGeometric([1,2,4,8,16,32,2]), False)	
		self.assertEqual(funcs.isGeometric([]), False)
		self.assertEqual(funcs.isGeometric([10]), False)

	def test_isArithmetic(self):
		self.assertEqual(funcs.isArithmetic([40,30,20,10]), True)
		self.assertEqual(funcs.isArithmetic([0,2,4,6,8,10]), True)
		self.assertEqual(funcs.isArithmetic([1,2,4,6,8,10]), False)
		self.assertEqual(funcs.isArithmetic([0,2,4,6,8,11]), False)
		self.assertEqual(funcs.isArithmetic([1,2,4,8,16,32]), False)
		self.assertEqual(funcs.isArithmetic([1]), False)
		self.assertEqual(funcs.isArithmetic([]), False)


	def test_nextGeo(self):
		self.assertEqual(funcs.nextGeo([24,12,6], 2), (True,[3,1]))
		self.assertEqual(funcs.nextGeo([1,2,4], 6), (True, [8, 16, 32, 64, 128, 256]))
		self.assertEqual(funcs.nextGeo([1,2,4], 0), (True,[]))
		self.assertEqual(funcs.nextGeo([1,3,9,12,15], 5), False)
		self.assertEqual(funcs.nextGeo([1,16,9,14,3], 3), False)
		self.assertEqual(funcs.nextGeo([1,2,4,8,16,32,2], 1), False)	
		self.assertEqual(funcs.nextGeo([], 4), False)
		self.assertEqual(funcs.nextGeo([10], 1), False)
		self.assertEqual(funcs.nextGeo([1,2,4], -6), False)

	def test_nextArith(self):
		self.assertEqual(funcs.nextArith([60,50,40], 4), (True, [30, 20, 10, 0]))
		self.assertEqual(funcs.nextArith([0,2,4,6,8,10], 3), (True, [12,14,16]))
		self.assertEqual(funcs.nextArith([0,2,4,6,8,10], 0), (True, []))
		self.assertEqual(funcs.nextArith([0,2,4,6,8,10], -3), False)
		self.assertEqual(funcs.nextArith([1,2,4,6,8,10], 3), False)
		self.assertEqual(funcs.nextArith([0,2,4,6,8,11], 3), False)
		self.assertEqual(funcs.nextArith([1,2,4,8,16,32], 3), False)
		self.assertEqual(funcs.nextArith([1], 5), False)
		self.assertEqual(funcs.nextArith([], 5), False)
if __name__ == '__main__':
	unittest.main()
