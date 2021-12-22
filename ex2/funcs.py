#!/usr/bin/python3
import sqlite3
import exdef

def connect() :
    conn = sqlite3.connect(exdef.DB_NAME)
    try :
         conn.cursor()
         return (True,conn)
    except Exception as ex:
         return (False,ex)

def create_table(table_name) :
    cur  = connect()[1].cursor()
    # At least one row must be specified when creating a table
    cur.execute("create table "+table_name+"(something)")
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='"+table_name+"'") 
    return cur.fetchall()[0][0]