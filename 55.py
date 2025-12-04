#Write a Python program to print a checkerboard pattern of stars. The size of the checkerboard should be taken as input as input from the user.

size = int(input("Enter the size of the checkerboard: "))

for i in range(size):
    line = ""
    for j in range(size):
        if (i + j) % 2 == 0:
            line += "*"
        else:
            line += " "
    print(line)

   