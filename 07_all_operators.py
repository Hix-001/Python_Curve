# ==========================================
# 1. ARITHMETIC OPERATORS
# ==========================================
print("\n--- 1. ARITHMETIC OPERATORS ---")
a = 10
b = 3
print(f"Values: a = {a}, b = {b}")

print("Addition (a + b):", a + b)
print("Subtraction (a - b):", a - b)
print("Multiplication (a * b):", a * b)
print("True Division (a / b):", a / b)
print("Floor Division (a // b):", a // b)
print("Modulus (a % b):", a % b)
print("Exponent (a ** b):", a ** b)


# ==========================================
# 2. ASSIGNMENT OPERATORS
# ==========================================
print("\n--- 2. ASSIGNMENT OPERATORS ---")
x = 5
print("Initial value: x = 5")

x += 2
print("After x += 2 (Add & Assign):", x)

x *= 3
print("After x *= 3 (Multiply & Assign):", x)

x //= 2
print("After x //= 2 (Floor Divide & Assign):", x)


# ==========================================
# 3. COMPARISON (RELATIONAL) OPERATORS
# ==========================================
print("\n--- 3. COMPARISON OPERATORS ---")
print(f"Values: a = {a}, b = {b}")

print("Equal to (a == b):", a == b)
print("Not equal to (a != b):", a != b)
print("Greater than (a > b):", a > b)
print("Less than or equal (a <= b):", a <= b)


# ==========================================
# 4. LOGICAL OPERATORS
# ==========================================
print("\n--- 4. LOGICAL OPERATORS ---")
# 'and' requires BOTH to be True
print("True and False :", True and False)

# 'or' requires AT LEAST ONE to be True
print("True or False  :", True or False)

# 'not' inverts the truth
print("not True       :", not True)


# ==========================================
# 5. IDENTITY OPERATORS
# ==========================================
print("\n--- 5. IDENTITY OPERATORS ---")
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1  # list3 points to the exact same memory location as list1

print("list1 is list3     :", list1 is list3)
print("list1 is list2     :", list1 is list2) # False, they are copies, not the exact same object!
print("list1 is not list2 :", list1 is not list2) 


# ==========================================
# 6. MEMBERSHIP OPERATORS
# ==========================================
print("\n--- 6. MEMBERSHIP OPERATORS ---")
repo_name = "Python_Curve"
print(f"Checking inside string: '{repo_name}'")

print("'Python' in repo_name :", "Python" in repo_name)
print("'Java' not in repo_name:", "Java" not in repo_name)


# ==========================================
# 7. BITWISE OPERATORS
# ==========================================
print("\n--- 7. BITWISE OPERATORS ---")
p = 2  # Binary: 10
q = 3  # Binary: 11
print(f"Values: p = {p} (Binary 10), q = {q} (Binary 11)")

print("Bitwise AND (p & q) :", p & q)
print("Bitwise OR (p | q)  :", p | q)
print("Bitwise XOR (p ^ q) :", p ^ q)
print("Bitwise NOT (~p)    :", ~p)
print("Left Shift (p << 1) :", p << 1)
print("Right Shift (p >> 1):", p >> 1)

