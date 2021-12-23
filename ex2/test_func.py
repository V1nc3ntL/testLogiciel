#!/usr/bin/python3
import funcs
import unittest
import sqlite3
from  exdef import *

class TestFuncs(unittest.TestCase):

    # Test are numbered as connection must be done first
    # The first 3 tests check that a proper database connection is set
    def test_00_connection(self):
        connected = self.assertTrue(funcs.connect()[0])
        if not connected :
            # Ensure that the tests won't go further if no connection can be set
            return -1

    def test_01_table_creation(self):
        # Compare the name of tables
        connected = self.assertEqual(funcs.create_table(TABLE_NAME),TABLE_NAME)
        if not connected :
            # Ensure that the tests won't go further if no table can be created
            return -1    

    def test_02_add_column(self):
        # Compare the name of columns
        for col in COLUMN_NAMES:
            self.assertEqual(funcs.add_column(col),col)

    # Exercises
    # Test for the user add function
    def test_03_add_user(self):
        for usr in WORKING_USERS:
            self.assertEqual(funcs.add_user(usr[0],usr[1]),(usr[0],usr[1]))

     # Test for the user add function
    def test_04_login(self):
        for usr in WORKING_USERS:
            self.assertTrue(funcs.login(usr[0],usr[1]))
        for usr_fault in FAULT_USERS:
            for usr in usr_fault :
                self.assertFalse(funcs.login(usr[0],usr[1]))
                
    def test_04_login(self):
        for usr in WORKING_USERS:
            self.assertTrue(funcs.login(usr[0],usr[1]))
        for usr_fault in FAULT_USERS:
            for usr in usr_fault :
                self.assertFalse(funcs.login(usr[0],usr[1]))

    def test_05_spubkeys(self):
        for usr in WORKING_USERS:
            self.assertEqual(funcs.get_spubkey(usr[0]),S_PUB_KEY)

    def test_06_sprikeys(self):
        for usr in WORKING_USERS:
            self.assertEqual(funcs.get_sprikey(usr[0]),S_PRI_KEY)

    def test_07_epubkeys(self):
        for usr in WORKING_USERS:
            self.assertEqual(funcs.get_epubkey(usr[0]),E_PUB_KEY)

    def test_08_epubkeys(self):
        for usr in WORKING_USERS:
            self.assertEqual(funcs.get_eprikey(usr[0]),E_PRI_KEY)


    
if __name__ == '__main__':

    unittest.main()