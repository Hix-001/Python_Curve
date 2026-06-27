info = {
    "key" : "value",
    "name" : "harsh",
    "learning" : "python",
    "age" : 20,
    "name" : "apna college",
    "is_adult" : True,
    "marks" : 98.93
}
print (info)
print (info["age"])
print(info["is_adult"])
print(info["marks"])
print(info["name"])    #This prints the last key value pair
print(type(info))
#_print (info["name","age"]) #This will raise an error because you cannot access multiple keys like this
print(info["age"], ["name"])  # prints 20 ['name'] because ['name'] is a list literal, not dict lookup
print(info["age"], info["name"])  # correct way to print both values


dict = {
    "name" : "apna college",
    "subjects" : ["python", "java", "rust"],
    "topics" : ("dictionaries","sets"),
}
print(dict)
print(dict["subjects"])
print(dict["topics"])
print(type(dict))


data = {
    12 : 322 , 872.972 : 8927.28,
}
print(data)
print("dictionaries are mutable but the keys of a dictionary must be immutable, hence we can use integers, strings, tuples, boolean, floats  as keys but not lists or sets as keys")
print(type(data))


dict2 = {
    "name" : "harsh", "age" : 20, "college" : "IILM",
}
dict2 ["name"] = "hats"         #overwrites
dict2 ["surname"] : "off"       #adds new key : value pair 
print (dict2)

null_dictionary = {}
print(null_dictionary)

