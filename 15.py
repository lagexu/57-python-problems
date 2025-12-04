#Write a Python program  to print the sum of all odd numbers from 1 to 50 using while loop.

total=0
count=1
while count<=50:
    if count%2 !=0:
        total += count
    count+=1
print(total)
