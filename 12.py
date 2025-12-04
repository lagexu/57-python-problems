#Write a Python program to check if a number is within a specific range.

number = float(input("Enter a number: "))
lower_bound = float(input("Enter the lower bound of the range: "))
upper_bound = float(input("Enter the upper bound of the range: "))

if lower_bound <= number <= upper_bound:
    print(f"{number} is within the range {lower_bound} to {upper_bound}.")
else:
    print(f"{number} is NOT within the range {lower_bound} to {upper_bound}.")
