#!/usr/bin/python3
import sqlite3
import exdef

def connect() :
    conn = sqlite3.connect()
    try :
         conn.cursor()
         return (True,conn)
    except Exception as ex:
         return (False,ex)