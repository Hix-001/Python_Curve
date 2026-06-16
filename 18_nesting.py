# x=int(input("Enter your age:"))
# if(x>=18):
#     if(x>=21):
#         print("You are eligible to drive")
#     else:
#         print("You are not eligible to drive")
# else :
#     print("You are not eligible to vote")


# Taking multiple interactive inputs
age = int(input("Enter player age: "))

if age >= 12:
    # ---- START OF NESTED CODE ----
    # 1. Take a second input for height here:
    height = int(input("Enter player height in cm: "))
    
    # 2. Write a nested if-else statement here to check if height is >= 140
    if (height >= 140):
        print("Access Granted: Full Motion VR Simulator!")
    else:
        print("Access Granted: Standard Handheld VR Zone.")
    # ---- END OF NESTED CODE ----
else:
    print("Access Denied: You must be at least 12 years old to enter the arcade.")