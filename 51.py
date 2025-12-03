# Number Pyramid Pattern
height = int(input("Enter the height of the traingle: "))
num=1
for i in range(1,height+1):
 for j in range(i):
  print(num,end=" ")
  num +=1
 print()