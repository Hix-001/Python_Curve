#str.endswith()
str="i am studing python with apna college"
print(str.endswith("ege"))                      #True
print(str.endswith("age"))                      #False

#str.capitalize()
string="samsung"
print(string.capitalize())
print(str)

stringcap="this is a string" 
strr = stringcap.capitalize()
print(strr)

#str.replace()
stringreplace="i am studing python from apna college"
print(stringreplace.replace("python","java"))
print(stringreplace.replace("a","A"))

#str.find()    #This method returns the index of the first occurrence of the specified substring. If the substring is not found, it returns -1.
stringfind="i am studing python from apna college"
print(stringfind.find("python"))    #Output: 14
print(stringfind.find("e"))         #Output: 28

#str.count()   #This method returns the number of occurrences of a specified substring in the string
stringcount="i am from iilm & i am studing python from apna college"
print(stringcount.count("i"))       
print(stringcount.count("from"))
print(stringcount.count("z"))
print(stringcount.count("i", 5, 20))   #This will count the occurrences of "i" in the substring from index 5 to index 20 (exclusive).


stringdex="i am from iilm"
print("the string ends with o :", stringdex.endswith("o",0,8))    #This will check if the substring from index 0 to index 7 (exclusive) ends with "o". Output: True
print(stringdex.find("i",0,-1))   #This will find the index of the first occurrence of "i" in the substring from index 0 to the second last character (exclusive). Output: 0
