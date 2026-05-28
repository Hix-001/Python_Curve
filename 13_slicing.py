str="apna college"      # Slicing syntax: string[start:stop:step]
                        # start: The index to start the slice (inclusive)
                        # stop: The index to end the slice (exclusive)
                        # step: The step size (optional, default is 1)
print(str[0:5])
print(str[5:11])
print(str[5:11])
print(str[5:1000])      # If stop index is greater than the string length, it will slice until the end of the string.
print(str[:4])
print(str[5:])
print(str[:])           # This will return the entire string.
print(str[len(str):4])  # This will return an empty string because the start index is greater than the stop index. 

str2="apna"
print(str2[-3:-1])      # This will return "pn" because it slices from index -3 to index -1 (exclusive) in reverse order.
print(str2[-3:])        # This will return "pna" because it slices from index -3 to the end of the string.
print(str2[:-1])        # This will return "apn" because it slices from the beginning of the string to index -1 (exclusive).
print(str2[-1:])        # This will return "a" because it slices from index -1 to the end of the string.
print(str2[-3])         # This will return "n" because it accesses the character at index -3 (the third character from the end of the string).
print(str2[-1:2])       # This will return an empty string because the start index (-1) is greater than the stop index (2).
print(str2[2:-1])       # This will return "n" because it slices from index 2 to index -1 (exclusive).
print(str2[0:-1])       # This will return "apn" because it slices from index 0 to index -1 (exclusive).
print(str2[-1:0])       # This will return an empty string because the start index (-1) is greater than the stop index (0).
print(str2[0:0])        # This will return an empty string because the start index (0) is equal to the stop index (0).