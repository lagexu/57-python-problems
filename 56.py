#Write a Python program to print an hourglass pattern of numbers. The size of the checkerboard should be taken as input as input from the user.

height = int(input("Enter the height of the hourglass: "))

for i in range(height, 0, -1):
    print(" " * (height - i), end="")
    for j in range(i,0,-1):
        print(j, end=" ")
    print()

for k in range(2,height+1):
 print(" "*(height-k),end="")
 for l in range(k,0,-1):
  print(l,end=" ")
 print()

