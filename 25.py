#Write a python program to print a multiplication table using nested loop.

for i in range(1,21):
    print(f"Multiplication table of {i}")
    for j in range(1,11):
        print(f"{i}x{j}={i*j}")
    print()