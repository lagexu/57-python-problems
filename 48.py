#Write a Python program to print an inverted right-angled triangle of stars.The height of the triangle should be taken as input from the user.

height = int(input("Enter Your Height: "))
for i in range(height,0,-1):
    print("*"*i)