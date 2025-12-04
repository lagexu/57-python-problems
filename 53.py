#Write a Python program to print a Hollow square pattern of letters.The size of the square should be taken as input from the user.

height = int(input("Enter the height of square: "))
alpha = ["A","B","C","D","E","F","G","H","I","J",
         "K","L","M","N","O","P","Q","R","S","T",
         "U","V","W","X","Y","Z"]

for i in range(0,height):
    for j in range(0,height):
       print(alpha[j],end=" ")
        
    print()