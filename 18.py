#Write a Python program to print the reverse of a given number using a while loop.

num = int(input("Enter Your Number: "))
rev = 0
while num > 0:
 digit = num % 10
 rev = rev*10+digit
 num //= 10
print(rev)