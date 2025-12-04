#Write a Python program to print a pyramid pattern of numbers.The height of the pyramid should be taken as input from the user.

height = int(input("Enter the height of the pyramid: "))
for i in range(1,height+1):
 print(" "*(height-i),end="")
 for j in range(1,i+1):
  print(j,end=" ")
 print()

   