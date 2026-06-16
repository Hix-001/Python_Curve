#Grade students based on their marks 
# marks>= 90, grade = "A"
# 90 > marks>= 80, grade = "B"
# 80 > marks>= 70, grade = "C"
# # 70 > marks, grade = "D"

x = int(input("Enter your marks:"))
if (x>=90):
    print("Grade: A")
elif (x>=80 and x<90):
    print("Grade: B")
elif (x>=70 and x<80):
    print("Grade: C")
else:    print("Grade: D")




x = int(input("Enter your marks:"))
if (x>100):
    print("Invalid marks")
elif (x>=90 and x<=100):
    print("Grade: A")
elif (x>=80 and x<90):
    print("Grade: B")
elif (x>=70 and x<80):
    print("Grade: C")
else:    print("Grade: D")