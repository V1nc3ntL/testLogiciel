#!/usr/bin/python3
import sqlite3
from exdef import  DB_NAME, TABLE_NAME, COLUMN_NAMES

cur = None

def connect(tst=True) :
    global cur 
    conn = sqlite3.connect(DB_NAME)
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
    query = "ALTER TABLE "+TABLE_NAME + " ADD COLUMN " + column_name + " " + type_str
    cur.execute(query)
    if(tst):
        cols = cur.execute("SELECT name FROM PRAGMA_TABLE_INFO('"+TABLE_NAME+"')" ).fetchall()
        if (column_name,) in cols :
            return column_name 
        else :
            return "" 

def add_user(usr_name,password,tst=True) :
    query = "INSERT INTO "+TABLE_NAME + "("+COLUMN_NAMES[0] + "," + COLUMN_NAMES[1] + ") values (?,?)" 
    cur.execute(query,(usr_name,password))
    if(tst):
        query = "SELECT "+ COLUMN_NAMES[0] +", " +COLUMN_NAMES[1]+ "  FROM "+TABLE_NAME+" WHERE "+COLUMN_NAMES[0] + " = '" +usr_name +"'"
        fields = cur.execute(query).fetchall()
        return fields[0]

def login(usr_name,password,tst=True) :
    query = "SELECT "+ COLUMN_NAMES[0] +", " +COLUMN_NAMES[1]+ "  FROM "+TABLE_NAME+" WHERE "+COLUMN_NAMES[0] + " = '" +usr_name +"'AND "+COLUMN_NAMES[1] + " = '" +password+"'" 
    fields = cur.execute(query).fetchall()
    print(fields)
    if fields :
        if(fields[0][0]==usr_name and fields[0][1]==password):
            return True
    return False