#Write a Python program to print all prime numbers between 1 and 100 using nested loops.

for i in range(2,101):
    isPrime=True
    for j in range(2,i):
        if (i%j)==0:
            isPrime=False
    
    if(isPrime):
        print(i)