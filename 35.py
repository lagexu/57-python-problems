# Write a Python program to demonstrate implicit and explicit type casting.

# -------- Implicit Type Casting --------
a = 10          # int
b = 3.5         # float

# Python automatically converts 'a' (int) to float for this operation
result = a + b  

print("Implicit Type Casting:")
print("a (int):", a)
print("b (float):", b)
print("result (a + b):", result, "|type:", type(result))


# -------- Explicit Type Casting --------
x = "25"        # string
y = int(x)      # explicitly casting string to int

z = float(y)    # explicitly casting int to float

print("\nExplicit Type Casting:")
print("x (string):", x)
print("y = int(x):", y, "|type:", type(y))
print("z = float(y):", z, "|type:", type(z))
