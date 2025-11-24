nTerms = int(input("How many terms? "))
count = 0
n1= 0
n2=1
while count<nTerms:
    print(n1)
    n1=n2
    nth = n1+n2
    n2=nth
    count +=1