#!/usr/bin/python3
import funcs
import unittest
import sqlite3
import exdef

class TestFuncs(unittest.TestCase):


    def test_connection(self):
        connected = self.assertTrue(funcs.connect()[0])
        if not connected :
            # Ensure that the tests won't go further if no connection can be set
            return -1

    def test_table_creation(self):
        # Compare the name of tables
        self.assertEqual(funcs.create_table(exdef.TABLE_NAME),exdef.TABLE_NAME)
        


if __name__ == '__main__':



    unittest.main()