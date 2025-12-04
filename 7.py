#Write a Python Program to check if a number is even or odd.
num = int(input("Enter Your Number: "))
if num == 0:
    print("Given Value is 0")
elif num % 2 == 0:
    print(f"{num} is an Even Number")
else:
    print(f"{num} is an Odd Number")

