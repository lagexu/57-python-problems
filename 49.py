# Number Pyramid Pattern
height = int(input("Enter the height of the pyramid: "))
value=""
for i in range(1,height+1):
 value=f"{value } {i }"
 print(" "*(height-i),end="")
 print(value)

   