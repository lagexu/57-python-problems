#Write a Python program to print Floyd's triangle.The number of rows should be taken as input from the user.

height = int(input("Enter the height of the traingle: "))
num=1
for i in range(1,height+1):
 for j in range(i):
  print(num,end=" ")
  num +=1
 print()