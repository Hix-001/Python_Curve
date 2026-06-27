#WAP to ask the user to enter name of their 3 favourite movie & store them in a list.
movies = []
mov1 = input("Enter the names of your 1st favourite movie: ")
mov2 = input("Enter the names of your 2nd favourite movie: ")
mov3 = input("Enter the names of your 3rd favourite movie: ")
movies.append(mov1)
movies.append(mov2)
movies.append(mov3)
print("Your favourute movies are :",movies)

#OR 

movies=[]
mov=input("Enter your 1st fav movie:")
movies.append(mov)  
mov=input("Enter your 2nd fav movie:")
movies.append(mov)
mov=input("Enter your 3rd fav movie:")
movies.append(mov)
print("Your favourute movies are :",movies)

#OR

movies=[]
movies.append(input("Enter your 1st fav movie:"))
movies.append(input("Enter your 2nd fav movie:"))
movies.append(input("Enter your 3rd fav movie:"))
print("Your favourute movies are :",movies)

#OR

movies = input("Enter your three favourite movies in three different strings separated by spaces: ").split()
print("Your favourite movies are :", movies)


#WAP to check if a list contains a plaindrome of elements in it or not.
#(A plaindrome is a word which reads the same from left to right and right to left)
#(Hint : use copy() method)

list = input("Enter list elements separated by spaces: ").split()
list1 = list.copy()
list1.reverse()
if list == list1:
    print("The given list is a palindrome")
else:
    print("The given list is not a palindrome")

#OR 

list = ["m", "a", "d", "a", "m"]
copy_list = list.copy()
copy_list.reverse()
if (list == copy_list):
    print("The given list is a palindrome")
else: 
    print("The given list is not a palindrome")



#WAP to count the number of students with the "A" grade in the following tuple :("A","C", "D" , "A" , "A" , "B" , "B" , "A") 
tup = ("A","C", "D" , "A" , "A" , "B" , "B" , "A")
print("Students with grade A in the tuple is :" , tup.count("A")) 

#WAP to sort tup into a list and sort them from "A" to "D" and print the sorted list 
tup = ("A","C", "D" , "A" , "A" , "B" , "B" , "A")
user = list(tup)
user.sort()
print(user)

tup = (4 , 6 , "D" , "A" , "A" , "B" , "B" , "A")
user = list(tup)
user.sort()                       #this will give TypeError as the tuple has both int and str 
print(user)

