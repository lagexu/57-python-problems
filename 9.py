# Write a Python program to find the largest of three numbers using nested if-else statements.

while True: 
    try:
        num1, num2, num3 = map(int, input("Enter 3 numbers separated by space: ").split())
        break
    except ValueError:
        print("Invalid input! Please enter exactly three numbers separated by spaces.")
if num1 >= num2:
    if num1 >= num3:
        largest = num1
    else:
        largest = num3
else:
    if num2 >= num3:
        largest = num2
    else:
        largest = num3
print(f"The largest number is {largest}")

