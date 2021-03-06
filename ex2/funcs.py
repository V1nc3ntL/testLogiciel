#!/usr/bin/python3
import sqlite3
from exdef import  *

cur = None
conn = None
def drop(table_name ,tst=True):
    cur.execute("DROP TABLE IF EXISTS "+table_name)
    if tst :
        try :
            cur.execute("SELECT * FROM " + table_name) 
            if cur.fetchall():
                return False
        except Exception as ex:
            return True 

def disconnect() :
    conn.close()
        
def connect(tst=True) :
    global cur,conn 
    conn = sqlite3.connect(DB_NAME)
    try :
        cur = conn.cursor()
        return True
    except Exception as ex:
        return False

def check_unique_username(table_name,usr_name="") :
    names = []
    if(not usr_name):
        cur.execute("SELECT username FROM "+table_name)
        usernames = cur.fetchall()
    else :
        usernames = usr_name

    for username in usernames :
        names.append(username[0])

    if(len(set(names)) != len(names)):
        return False
    return True

def check_special_username(table_name,usr_name="") :
    names = []
    if(not usr_name):
        cur.execute("SELECT username FROM "+table_name)
        usernames = cur.fetchall()
    else :
        usernames = usr_name
        
    for username in usernames :
        if (any(not c.isalnum() for c in username)):
            return False
    return True

def check_length_username(table_name,usr_name="") :
    names = []
    if(not usr_name):
        cur.execute("SELECT username FROM "+table_name)
        usernames = cur.fetchall()
    else :
        usernames = usr_name
        
    for username in usernames :
        if len(username[0]) <= MIN_USERNAME_LENGTH:
            return False
    return True


def check_length_password(table_name,pwds="") :
    names = []
    if(not pwds):
        cur.execute("SELECT password FROM "+table_name)
        passwords = cur.fetchall()
    else :
        passwords = pwds

    for pwd in passwords :
        if len(pwd[0]) < MIN_PASSWORD_LENGTH:
            return False
    return True

def check_upper_password(table_name,pwds="") :
    names = []
    if(not pwds):
        cur.execute("SELECT password FROM "+table_name)
        passwords = cur.fetchall()
    else :
        passwords = pwds
    
    for pwd in passwords :
       res = any(c.isupper() for c in pwd[0])
       if not res :
           return False
    
    return True

def check_digit_password(table_name,pwds="") :
    names = []
    if(not pwds):
        cur.execute("SELECT password FROM "+table_name)
        passwords = cur.fetchall()
    else :
        passwords = pwds
    
    for pwd in passwords :
       res = any(c.isdigit() for c in pwd[0])
       if not res :
           return False
    return True


def check_standard_password(table_name,pwds="") :
    names = []
    if(not pwds):
        cur.execute("SELECT password FROM "+table_name)
        passwords = cur.fetchall()
    else :
        passwords = pwds
    
    for pwd in passwords :
       res = any(c.islower() for c in pwd[0])
       if not res :
           return False
    return True
    
def check_len_key(table_name,key_col_name,keys_str="") :
    names = []
    if(not keys_str):
        cur.execute("SELECT "+key_col_name+" FROM "+table_name)
        passwords = cur.fetchall()
    else :
        passwords = keys_str

    for key in passwords :
        if len(key[0]) < KEY_SIZE :
                return False
    return True

def validate(table):
    
    res = []
    cur.execute("SELECT username FROM "+table)
    usrs = cur.fetchall()
    
    res.append(check_length_username(table,usrs))
    res.append(check_unique_username(table,usrs))
    res.append(check_special_username(table,usrs))
  
    cur.execute("SELECT password FROM "+table)
    passwords = cur.fetchall()
    res.append(check_length_password(table,passwords))
    res.append(check_upper_password(table,passwords))
    res.append(check_length_password(table,passwords))
    res.append(check_digit_password(table,passwords))
    res.append(check_standard_password(table,passwords))

    res.append(check_len_key(table,S_PRI_KEY_COL_NAME))
    res.append(check_len_key(table,S_PRI_KEY_COL_NAME))
    res.append(check_len_key(table,E_PUB_KEY_COL_NAME))
    res.append(check_len_key(table,E_PRI_KEY_COL_NAME))

    if False in res :
        return False
    
    return True


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

    