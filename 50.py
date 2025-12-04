#Write a Python program to print a diamond pattern of stars.The height of the diamond should be taken as input from the user.

height = int(input("Enter the height of the diamond: "))

for i in range(1,height+1):
  print(" "*(height-i),end="")
  print("* "*i)


for j in range(height-1,0,-1):
 print(" "*((height-j)),end="")
 print("* "*j)

   