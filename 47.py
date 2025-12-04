#Write a Python program to print a right-angled triangle of numbers.The Height of the triangle should be taken as input from the user.

height = int(input("Enter Your Height: "))
value = 0
for i in range(1,height+1):
    value= (value*10)+i
    print(value)
