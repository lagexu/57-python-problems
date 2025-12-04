#Write a Python program to check if a number is palindrome or not.

num = input("Enter Your Number: ")

rev = "".join(reversed(num))

if num == rev:
    print("Given number is palindrome.")
else:
    print("Given number isn't a palindrome.")
