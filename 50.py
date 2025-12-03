# Number Pyramid Pattern
height = int(input("Enter the height of the diamond: "))

for i in range(1,height+1):
  print(" "*(height-i),end="")
  print("* "*i)


for j in range(height-1,0,-1):
 print(" "*((height-j)),end="")
 print("* "*j)

   