#Auto pacing
import random,time
import numpy as np

TPH = 100
Users = 5

#simulating jmeter script
x = []
y = []
for i in range(TPH):
    #Simulating script iteration end to end response time
    E2E = random.randint(300,500)
    #time.sleep(E2E)
    print(str(i)+" iteration has completed")

    #Simulating pacing time
    Pacing = 3600/(TPH/Users) - E2E
    if(Pacing < 0):
        Pacing = 0
    print("wait time untill next iteration is "+str(Pacing)+" seconds")
   #time.sleep(Pacing)
    print("Next iteration started")
    x.append(E2E)
    y.append(Pacing)
print(x)
print(y)
X_sum = sum(x)
Y_sum = sum(y)
print(X_sum)
print(Y_sum)
Total_Time = (X_sum + Y_sum)/Users
print("Total Time= "+str(Total_Time))