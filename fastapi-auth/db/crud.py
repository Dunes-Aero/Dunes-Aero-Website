import sqlite3
from sqlite3 import Error


con = sqlite3.connect('users.db')
cur = con.cursor()
try:
   cur.execute("CREATE TABLE USERS(ID INTEGER PRIMARY KEY, EMAIL TEXT, NAME TEXT, PASSWORD TEXT)")
except Error as e:
   print(e)

# #verify table existence 
# res = cur.execute("SELECT name FROM sqlite_master")
# res.fetchall()

user_1 = ( 'haya ffff', 'WEWEW@gmail.com', 'PASSWORD')
sql = ''' INSERT INTO USERS(NAME,EMAIL,PASSWORD)
            VALUES(?,?,?) '''
cur = con.cursor()
cur.execute(sql, user_1)
con.commit()

cur.execute("SELECT * FROM USERS")
rows = cur.fetchall()
for row in rows:
   print(row)




def create_connection(db_file):
    con = None
    try: 
        con = sqlite3.connect(db_file)
    except Error as e:
        raise Exception(e)

    return con


def create_table(con):
    cur = con.cursor()
    try:
     cur.execute("CREATE TABLE USERS(ID INTEGER PRIMARY KEY, EMAIL TEXT, NAME TEXT, PASSWORD TEXT)")
    except Error as e:
     raise Exception(e)
    

#generate random is string of 8 digits
#insert id, name,email, pass o=into db
#return a success flag 
def addUser(con,password,email):

    pass




def loginUser(email,password, con):
    name = None
    cur = con.cursor()
    try:
        cur.execute("SELECT NAME FROM USERS WHERE EMAIL=? AND PASSWORD=? ", (email,password))
        row = cur.fetchone()
        if row !=None:
            name = row[0]
    except Error as e:
      raise Exception("Error had occured")
    return name



def searchUser(email, con):
    cur = con.cursor()
    res= None
    try:
        cur.execute("SELECT NAME FROM USERS WHERE EMAIL=?", (email,))
        res = cur.fetchone()
    except Error as e:
      raise Exception(e)
    return res
    


    