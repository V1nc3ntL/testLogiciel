#!/usr/bin/python3
import sqlite3
import exdef

cur = None

def connect(tst=True) :
    global cur 
    conn = sqlite3.connect(exdef.DB_NAME)
    try :
        cur = conn.cursor()
        return (True,conn)
    except Exception as ex:
        return (False,ex)

def create_table(table_name,tst=True) :
    # At least one row must be specified when creating a table
    cur.execute("create table "+table_name+"(s)")
    if(tst):
        cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='"+table_name+"'") 
        return cur.fetchall()[0][0]

def add_column(column_name,type_str="STRING",tst=True) :
    query = "ALTER TABLE "+exdef.TABLE_NAME + " ADD COLUMN " + column_name + " " + type_str
    cur.execute(query)
    if(tst):
        cols = cur.execute("SELECT name FROM PRAGMA_TABLE_INFO('"+exdef.TABLE_NAME+"')" ).fetchall()
        if (column_name,) in cols :
            return column_name 
        else :
            return "" 

def add_user(usr_name,password,tst=True) :
    return ""