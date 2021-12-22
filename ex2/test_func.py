#!/usr/bin/python3
import funcs
import unittest
import sqlite3
import exdef

class TestFuncs(unittest.TestCase):


    def test_00_connection(self):
        connected = self.assertTrue(funcs.connect()[0])
        if not connected :
            # Ensure that the tests won't go further if no connection can be set
            return -1

    def test_01_table_creation(self):
        # Compare the name of tables
        connected = self.assertEqual(funcs.create_table(exdef.TABLE_NAME),exdef.TABLE_NAME)
        if not connected :
            # Ensure that the tests won't go further if no table can be created
            return -1    

    def test_02_add_column(self):
        # Compare the name of columns
        for col in exdef.COLUMN_NAMES:
            self.assertEqual(funcs.add_column(col),col)


if __name__ == '__main__':

    unittest.main()