import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="mydatabase"
)

mycursor = mydb.cursor()

def dbFetch(name):
    mycursor.execute(f"SELECT Task,comments FROM tasks WHERE UserName='{name}'")
    print(mycursor.fetchall())
def dbPush(name,task,comment):
    mycursor.execute(f"INSERT INTO tasks (UserName,Task,comments) values('{name}','{task}','{comment}')")
    mydb.commit()

