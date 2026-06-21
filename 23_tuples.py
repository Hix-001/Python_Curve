# tup = (23, 25, 39, 45, 56)
# print(type(tup))
# print(tup[0])
# print(tup[-1])
# print("length of tuple is :",len(tup))

# #tup[0] = 100   This produces an error because tuples are immutable.

# tup1=() #empty tuple
# print(tup1)
# print(type(tup1))

# tup2=(1,) #tuple with one element
# print(tup2)
# print(type(tup2))

# tup3=(1) #this is not a tuple, it's an integer
# print(tup3) 
# print(type(tup3)) 

# tup4=("hello")
# print(tup)
# print(type(tup)) #this is not a tuple, it's a string

# tup5=("hello",) #this is a tuple with one element
# print(tup5)
# print(type(tup5))

# tup6=(1,2,3,4,5,) #the comma at the end is optional
# print(tup6)

# tup7=(1,2,3,4,5)
# print(tup7)

tuple = (1,2,3,4,5)
print(tuple[0:3])  #O/p: (1, 2, 3)
print(tuple[1:])   
print(tuple[:-1])
print(tuple[:])
