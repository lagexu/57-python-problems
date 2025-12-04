#Write a Python program to print a Hollow square pattern of stars.The size of the square should be taken as input from the user.

height = int(input("Enter the height of the square: "))

for i in range(height):
    for j in range(height):
        # Print star on borders, space inside
        if i == 0 or i == height - 1 or j == 0 or j == height - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
