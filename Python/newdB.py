import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="mydatabase"
)

mycursor = mydb.cursor()

def createUser(UserName,phonenumber,salt,hash_password,comments):
    inser_query = "INSERT INTO userdata (UserName,phonenumber,salt,hash_password,comments) values(%s,%s,%s,%s,%s)"
    insert_data = (UserName,phonenumber,salt,hash_password,comments)
    mycursor.execute(inser_query,insert_data)
    mydb.commit()

def validateUser(UserName):
    insert_query = "SELECT hash_password FROM userdata WHERE UserName = %s"
    mycursor.execute(insert_query,(UserName,))
    hash_password = mycursor.fetchone()
    global fetch_hash_password
    fetch_hash_password = hash_password[0]
    

def dbFetch(name):
    mycursor.execute(f"SELECT Task,comments FROM tasks WHERE UserName='{name}'")
    myTasks = mycursor.fetchall()
    for task,comment in myTasks:
        print(f"title= {task}, comments= {comment}")

def dbPush(name,task,comment):
    mycursor.execute(f"INSERT INTO tasks (UserName,Task,comments) values('{name}','{task}','{comment}')")
    mydb.commit()

