#Write a Python program to reverse a string.

string = input("Enter Your Word: ") #dog
length = len(string)
rev=''
for i in range (1,length+1):
    rev += string[length-i]

print(rev)