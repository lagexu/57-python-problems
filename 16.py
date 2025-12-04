#Write a Python program to print the multiplication table of a given number using for loop.
num = int(input("Enter Your Number: "))
for i in range(1,11):
    print(f"{num}x{i} = {num*i}")

