#Write a Python program to print the Fibonacci series up to specified number of terms using a while loop.

nTerms = int(input("How many terms? "))
count = 0
n1= 0
n2=1
while count<nTerms:
    print(n1)
    nth = n1+n2
    n1=n2
    n2=nth
    count +=1