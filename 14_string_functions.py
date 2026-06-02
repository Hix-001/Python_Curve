# str.endswith()
text = "i am studying python with apna college"
print(text.endswith("ege"))                      # True
print(text.endswith("age"))                      # False

# str.capitalize()
company = "samsung"
print(company.capitalize())
print(text)

sentence = "this is a string"
capitalized_sentence = sentence.capitalize()
print(capitalized_sentence)

# str.replace()
replace_example = "i am studying python from apna college"
print(replace_example.replace("python", "java"))
print(replace_example.replace("a", "A"))

# str.find()    # returns the index of the first occurrence of the specified substring. If the substring is not found, it returns -1.
find_example = "i am studying python from apna college"
print(find_example.find("python"))    # Output: 14
print(find_example.find("e"))         # Output: 28

# str.count()   # returns the number of occurrences of a specified substring in the string
count_example = "i am from iilm & i am studying python from apna college"
print(count_example.count("i"))       
print(count_example.count("from"))
print(count_example.count("z"))
print(count_example.count("i", 5, 20))   # Count "i" in the substring from index 5 to 20 (exclusive).

stringdex = "i am from iilm"
print("the string ends with o :", stringdex.endswith("o", 0, 8))    # Checks if the substring from index 0 to 8 (exclusive) ends with "o". Output: True
print(stringdex.find("i", 0, -1))
