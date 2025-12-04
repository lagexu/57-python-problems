#Write Python program to check if a string is palindrome.

string = input("Enter Your String: ")

rev = "".join(reversed(string))

if string == rev:
    print("Given string is palindrome.")
else:
    print("Given string isn't a palindrome.")
