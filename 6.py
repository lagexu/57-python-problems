#Write a python program to count the number of times a specified value appears in a string.
string = input("Enter your string: ")
value = input("Enter the value you want to count: ")
count = string.count(value)
print(f"'{value}' appears {count} time(s) in the string.")
