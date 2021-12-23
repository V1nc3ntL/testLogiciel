#!/usr/bin/python3
import funcs
import unittest
import sqlite3
from  exdef import *

class TestFuncs(unittest.TestCase):

    
   

    # Exercises
    # 01
    # Test for the user add function
    def test_04_add_user(self):
        for usr in WORKING_USERS:
            self.assertEqual(funcs.add_user(usr[0],usr[1]),(usr[0],usr[1]))
    # 02
     # Test for the user add function
    def test_05_login(self):
        for usr in WORKING_USERS:
            self.assertTrue(funcs.login(usr[0],usr[1]))
        for usr_fault in FAULT_USERS:
            for usr in usr_fault :
                self.assertFalse(funcs.login(usr[0],usr[1]))
                
    # 03
    def test_06_spubkeys(self):
        for usr in WORKING_USERS:
            self.assertEqual(funcs.get_spubkey(usr[0]),S_PUB_KEY)

    def test_07_sprikeys(self):
        for usr in WORKING_USERS:
            self.assertEqual(funcs.get_sprikey(usr[0]),S_PRI_KEY)

    def test_08_epubkeys(self):
        for usr in WORKING_USERS:
            self.assertEqual(funcs.get_epubkey(usr[0]),E_PUB_KEY)

    def test_09_epubkeys(self):
        for usr in WORKING_USERS:
            self.assertEqual(funcs.get_eprikey(usr[0]),E_PRI_KEY)
    # 04
    def test_10_unique_username(self):
        self.assertTrue(funcs.check_unique_username(TABLE_NAME))
        funcs.add_user(FAULT_USERNAME_UNIQUE[0],FAULT_USERNAME_UNIQUE[1])
        self.assertFalse(funcs.check_unique_username(TABLE_NAME))
    
    def test_11_length_username(self):
        self.assertTrue(funcs.check_length_username(TABLE_NAME))
        funcs.add_user(FAULT_USERNAME_LENGTH[0],FAULT_USERNAME_LENGTH[1])
        self.assertFalse(funcs.check_length_username(TABLE_NAME))

    def test_12_special_username(self):
        self.assertTrue(funcs.check_special_username(TABLE_NAME))
        funcs.add_user(FAULT_USERNAME_SPECIALCHAR[0],FAULT_USERNAME_SPECIALCHAR[1])
        self.assertFalse(funcs.check_special_username(TABLE_NAME))

    def test_13_length_password(self):
        self.assertTrue(funcs.check_length_password(TABLE_NAME))
        funcs.add_user(FAULT_PASSWORD_LENGTH[0],FAULT_PASSWORD_LENGTH[1])
        self.assertFalse(funcs.check_length_password(TABLE_NAME))

    def test_31_drop(self):
        self.assertTrue(funcs.drop(TABLE_NAME))

    def test_32_add_column(self):
        # Compare the name of columns
        funcs.create_table(TABLE_NAME)
        for col in COLUMN_NAMES:
            self.assertEqual(funcs.add_column(col),col)


    def test_33_table_creation(self):
        # Compare the name of tables
        self.assertEqual(funcs.create_table("tst"),"tst")

    def test_34_connection(self):
        # this function just calls a sqlite function
        # so it is not tested
        funcs.disconnect()
        connected = self.assertTrue(funcs.connect())
        if not connected :
            # Ensure that the tests won't go further if no connection can be set
            return -1
    
if __name__ == '__main__':
    
    funcs.connect(False)
    funcs.drop(TABLE_NAME)
    funcs.create_table(TABLE_NAME)
    for col in COLUMN_NAMES:
           funcs.add_column(col)
    unittest.main()