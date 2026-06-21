# #WAP to ask the user to enter name of their 3 favourite movie & store them in a list.
# movies = []
# mov1 = input("Enter the names of your 1st favourite movie: ")
# mov2 = input("Enter the names of your 2nd favourite movie: ")
# mov3 = input("Enter the names of your 3rd favourite movie: ")
# movies.append(mov1)
# movies.append(mov2)
# movies.append(mov3)
# print("Your favourute movies are :",movies)

# #OR 

# movies=[]
# mov=input("Enter you 1st fav movie:")
# movies.append(mov)
# mov=input("Enter you 2nd fav movie:")
# movies.append(mov)
# mov=input("Enter you 3rd fav movie:")
# movies.append(mov)
# print("Your favourute movies are :",movies)

# #OR

# movies=[]
# movies.append(input("Enter you 1st fav movie:"))
# movies.append(input("Enter you 2nd fav movie:"))
# movies.append(input("Enter you 3rd fav movie:"))
# print("Your favourute movies are :",movies)



#WAP to check if a list contains a plaindrome of elements in it or not.
#(A plaindrome is a word which reads the same from left to right and right to left)
#(Hint : use copy() method)

list = [1,"abc","abc",1]
list1 = list.copy()
list1.reverse()
if (list1 == list) : 
	print ( "The given list is a palindrome")
else : 
	print("The given list is not a palindrome")