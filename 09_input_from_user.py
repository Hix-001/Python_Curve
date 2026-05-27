input("Enter your name: ")  #returns a string value

name = input("Enter your name: ")  #returns a string value and stores it in the variable 'name'
print("Hello, ", name)  # Greet the user by name

val=input("Enter a value: ")
print(type(val), val)  #"25" "99.99" converts any value given by user into a string by default

#=========================================================================================================
 
int(input("Enter your age: "))  #returns an integer value

val=int(input("Enter your age: "))
print(type(val), val)

#=========================================================================================================

float(input("Enter your height in meters: "))  #returns a float value

val=float(input("Enter your height in meters: "))  #value error if user enters a non-numeric value
print(type(val), val)