#Write a Python program to calculate the factorial of a number using a while loop.

num = int(input("Enter Your Number: "))

factorial = 1
count = 1
while count<=num:
    factorial *= count
    count +=1
print(factorial)
