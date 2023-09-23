import time
import newdB

def toDolist():

 while True:
    
    print("\nSelect the following number to perform any operation")

    try:
        #Prompting user for input
        userInput = int(input("1.Add task, 2.Show all tasks,  3.Remove task, 4.Clear all tasks, 5.Quit \n"))

        #Add task
        if(userInput == 1):
          name = str(input("Enter your name \n"))
          task = str(input("Enter your task \n"))
          comment = str(input("Enter your comments \n"))
          newdB.dbPush(name,task,comment)
          print("Task Added successfully :)")

        #Show all the tasks
        elif(userInput == 2):
          name = str(input("Enter your full name:-"))
          print("\nTasks:-")
          newdB.dbFetch(name)
        
        #delete a specific task
        elif(userInput == 3):
          print("\nSelect a task to delete from below list")
          
        
        #Clear all the tasks
        elif(userInput == 4):
          print("Successfully deleted all the task")
        
        #Exit
        elif(userInput == 5):
          newdB.mydb.close()
          break
        
        #User input handling
        elif(userInput > 5 or userInput <= 0):
          print("Invalid selection, number should be between 1 and 4")

    except (ValueError,IndexError):
      print("invalid input")