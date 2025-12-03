# Number Pyramid Pattern
height = int(input("Enter the height of the pyramid: "))
uppervalue=""
lowervalue=""
for j in range(height,0,-1):
 for k in range(j,0,-1):
  uppervalue=f"{uppervalue } {j }"
 print(" "*(height-j),end="")
 print(uppervalue)
# for i in range(1,height+1):
#  lowervalue=f"{lowervalue } {i }"
#  print(" "*(height-i),end="")
#  print(lowervalue)

   