# Number Pyramid Pattern
height = int(input("Enter the height of the pyramid: "))

for i in range(height):
    # Print leading spaces
    print(' ' * (height - i), end='')
    num = 1
    for j in range(i + 1):
        print(num, end=' ')
            # Compute the next number in the row
        num = num * (i - j) // (j + 1)
    print()

