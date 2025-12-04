#Write a Python program to print Pascal's triangle.The number of rows should be taken as input from the user.

height = int(input("Enter the height of the triangle: "))

for i in range(height):

    print(' ' * (height - i), end='')
    num = 1
    for j in range(i + 1):
        print(num, end=' ')
        num = num * (i - j) // (j + 1)
    print()

