#!/usr/bin/python3
import sqlite3
from exdef import  DB_NAME, TABLE_NAME, COLUMN_NAMES,\
S_PUB_KEY,S_PRI_KEY,E_PUB_KEY,E_PRI_KEY,KEY_NAMES,\
USERNAME_COL_NAME, PASSWORD_COL_NAME,S_PUB_KEY_COL_NAME,\
S_PRI_KEY_COL_NAME,E_PUB_KEY_COL_NAME,E_PRI_KEY_COL_NAME

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

def add_column(column_name,fixed_len=128,tst=True) :
    query = "ALTER TABLE "+TABLE_NAME + " ADD COLUMN " + column_name + " " 
    if(column_name in KEY_NAMES):
        query+=" CHAR("+ str(fixed_len)+")"
    else:
        query+=" VARCHAR("+ str(fixed_len)+")"
    cur.execute(query)
    if(tst):
        cols = cur.execute("SELECT name FROM PRAGMA_TABLE_INFO('"+TABLE_NAME+"')" ).fetchall()
        if (column_name,) in cols :
            return column_name 
        else :
            return "" 

def add_user(usr_name,password,tst=True,spub=S_PUB_KEY,spri=S_PRI_KEY,epub=E_PUB_KEY,epri=E_PRI_KEY) :
    query = "INSERT INTO "+TABLE_NAME + "(" +COLUMN_NAMES[0]
    var_field = "(?"
    for col in COLUMN_NAMES[1:] :
        query +=   " , " + col 
        var_field += ",?"

    query += ") values " + var_field+")"
    cur.execute(query,(usr_name,password,spub,spri,epub,epri))
    if(tst):
        query = "SELECT "+ USERNAME_COL_NAME +", " + PASSWORD_COL_NAME + "  FROM "+TABLE_NAME+" WHERE "+USERNAME_COL_NAME + " = '" +usr_name +"'"
        fields = cur.execute(query).fetchall()
        return fields[0]

def login(usr_name,password) :
    query = "SELECT "+ USERNAME_COL_NAME +", " + PASSWORD_COL_NAME + "  FROM "+TABLE_NAME+" WHERE "+USERNAME_COL_NAME + " = '" +usr_name +"'AND "+PASSWORD_COL_NAME+ " = '" +password+"'" 
    fields = cur.execute(query).fetchall()
    if fields :
        if(fields[0][0]==usr_name and fields[0][1]==password):
            return True
    return False


def get_spubkey(usr_name,tst=True) :
    query = "SELECT "+ S_PUB_KEY_COL_NAME +"  FROM "+TABLE_NAME+" WHERE "+USERNAME_COL_NAME + " = '" +usr_name +"'"
    fields = cur.execute(query).fetchall()
    if fields :
        return fields[0][0]
    return ""
    
def get_sprikey(usr_name,tst=True) :
    query = "SELECT "+ S_PRI_KEY_COL_NAME +"  FROM "+TABLE_NAME+" WHERE "+USERNAME_COL_NAME + " = '" +usr_name +"'"
    fields = cur.execute(query).fetchall()
    if fields :
        return fields[0][0]
    return ""
    
def get_epubkey(usr_name,tst=True) :
    query = "SELECT "+ E_PUB_KEY_COL_NAME  +"  FROM "+TABLE_NAME+" WHERE "+USERNAME_COL_NAME + " = '" +usr_name +"'"
    fields = cur.execute(query).fetchall()
    if fields :
        return fields[0][0]
    return ""
    
def get_eprikey(usr_name,tst=True) :
    query = "SELECT "+ E_PRI_KEY_COL_NAME+"  FROM "+TABLE_NAME+" WHERE "+USERNAME_COL_NAME + " = '" +usr_name +"'"
    fields = cur.execute(query).fetchall()
    if fields :
        return fields[0][0]
    return ""

    