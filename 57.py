#Write a Python program to print a pattern of alphabets in decresing order.The height of the patterns should be taken as input from the user.

height = int(input("Enter Your Height: "))
alpha = ["A","B","C","D","E","F","G","H","I","J",
         "K","L","M","N","O","P","Q","R","S","T",
         "U","V","W","X","Y","Z"]
for i in range(height,0,-1):
    for j in range(i,0,-1):
        print(alpha[j-1],end=' ')
    print()