#IF CONDITION 
age = 18 
if(age >= 18):
    print("You are eligible to vote.")

age = 16
if(age >= 18):
    print("You are eligible to vote.")

age = 25
if(age >= 18):
    print("can drive")
    print("can vote")

age = 15
if(True):
    print("can drive can vote")             #This will execute as the condition is true.

age = 24
if(False):
    print("can drive can vote")             #This will execute nothing as the condition is false.


#ELIF CONDITION [ELIF = ELSE IF]
light ="green"
if(light == "red"):
    print("stop")
elif(light == "yellow"):
    print("get ready")
elif(light == "green"):
    print("go")

    #Note : elif condition is only checked when the previous if or elif condition is false. 
    # If the previous condition is true, then the elif condition will not be checked.
num = 5
if(num >2):
    print("greater than 2")
if(num >3):
    print("greater than 3")
elif(num>0):
    print("zero")

#ELSE CONDITON
#it is onlhy used once at the end of if-elif ladder and it will execute when all the previous conditions are false.

light = "blue"
if(light == "red"):
    print("stop")  
elif(light == "yellow"):
    print("get ready")
elif(light == "green"):
    print("go")
else:
    print("invalid light")

age = int(input("Enter your age: "))
if(age >= 18):
    print("can drive")
else:
    print("cannot drive")

