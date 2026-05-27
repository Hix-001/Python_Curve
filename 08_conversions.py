#type conversion
a=20
b=7.7
sum=a+b
print(sum) # this will print 27.7 because Python automatically converts the integer to a float

# Explicit type conversion (casting)
a=int(20)  # a is already an integer, but this is how you would explicitly convert it
b=float(7.7)  # b is already a float, but this is how you would explicitly convert it
print(a)  # prints 20
print(b)  # prints 7.7
print(type(a))  # prints <class 'int'>
print(type(b))  # prints <class 'float'>
print(a + b)  # prints 27.7, the integer is converted to a float for the addition


a=3.14
a=str(a)  # Convert the float to a string
print(a)  # prints '3.14'
print(type(a))  # prints <class 'str'>