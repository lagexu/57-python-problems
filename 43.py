#Write a Python program to generate the Fibonacci sequence up to a specified number of terms.

nTerms = int(input("How many terms? "))

count = 0
n1 = 0
n2 = 1

while count < nTerms:
    print(n1)
    nth = n1 + n2
    n1 = n2
    n2 = nth
    count += 1
