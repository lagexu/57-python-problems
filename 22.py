num = int(input("Enter Your Number: "))
sumOfDigits=0
while num >0:
 digit = num%10
 sumOfDigits += digit
 num //=10

print(sumOfDigits)