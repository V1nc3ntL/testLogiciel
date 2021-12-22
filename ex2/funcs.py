#!/usr/bin/python3
import sqlite3

DB_NAME = "ex2TDD.db"

def connect() :
    conn = sqlite3.connect()
    try :
        conn.cursor()
        return True
    except Exception :
        return False
    