#Write a Python program to check if a number is armstrong or not.

num = input("Enter Your Number: ")
originalNum = int(num)   
numLen = len(num)

count = 0
sumArm = 0

while count < numLen:
    digit = int(num[count])
    sumArm += digit ** numLen
    count += 1

if sumArm == originalNum:
    print(f"{num} is an Armstrong Number!")
else:
    print(f"{num} is NOT an Armstrong Number.")