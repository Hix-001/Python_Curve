str = "hello world"

# 1. Forward Indexing (0 to 10)
print(f"The first character is: {str[0]}")  # Output: h
print(f"The 7th character is: {str[6]}")    # Output: w (Space is at index 5!)

# 2. Backward Indexing (-1 to -11)
print(f"The last character is: {str[-1]}")  # Output: d
print(f"The character at -3 is: {str[-3]}") # Output:  (the space character)

# 3. Quick Tip: Strings are immutable
# You cannot change a character once it's set:
# str[0] = "H"  <-- This would raise a TypeError