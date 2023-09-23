import bcrypt
import newdB
import matplot

def userRegister():
        #prompting username and phone number
        UserName = str(input("Enter your username\n"))
        phonenumber = str(input("enter your phonenumber\n"))
        #prompting and hashing the password
        while True:
         password = str(input("Enter your password\n"))
         re_password = str(input("re enter your password\n"))
         if(password == re_password):
            salt = bcrypt.gensalt()
            hash_password = bcrypt.hashpw(password.encode("utf=-8"),salt)
            comments = "Add some comment"
            newdB.createUser(UserName,phonenumber,salt,hash_password,comments)
            print("registration successful")
            break
         else: print("password doesn't match, try again")

def userSignIn():
   login_username = str(input("Enter ur name\n"))
   login_password = str(input("Enter ur password\n"))
   try:
     newdB.validateUser(login_username)
     if(bcrypt.checkpw(login_password.encode("utf-8"),newdB.fetch_hash_password.encode("utf-8"))):
        print("login successful")
        matplot.toDolist()
     else:
        print("login failed password is wrong")
   except TypeError:
      print("Username or password is wrong")



        
print("Welcome to toDoList")
print("1.Register, 2.signin")
userinput = int(input("Enter your selection"))
if (userinput == 1):
    userRegister()
elif (userinput==2):
    userSignIn()