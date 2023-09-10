import sqlite3
from sqlite3 import Error
# con = sqlite3.connect('users.db')
# cur = con.cursor()
# cur.execute("CREATE TABLE USERS(ID, EMAIL, NAME, PASSWORD)")

# #verify table existence 
# res = cur.execute("SELECT name FROM sqlite_master")
# res.fetchall()

# user_1 = ('123', 'haya', 'haya@gmail.com', 'password123')
# sql = ''' INSERT INTO USERS(ID,NAME,EMAIL,PASSWORD)
#             VALUES(?,?,?,?) '''
# cur = con.cursor()
# cur.execute(sql, user_1)
# con.commit()

# cur.execute("SELECT * FROM USERS")
# rows = cur.fetchall()
# for row in rows:
#    print(row)




def create_connection(db_file):
    con = None
    try: 
        con = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return con


def create_table():
    cur = con.cursor()
    try:
     cur.execute("CREATE TABLE USERS(ID, EMAIL, NAME, PASSWORD)")
    except Error as e:
     print(e)
    


def addUser():

    pass




def searchUser(email,password):
    name = None
    try:
        cur.execute("SELECT NAME FROM USERS WHERE EMAIL=? AND PASSWORD=? ", (email,password))
        row = cur.fetchone()
        name = row[0]
    except Error as e:
      print(e)
    return name

    


    