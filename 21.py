num = input("Enter Your Number: ") # '153'
numLen = len(num) #3
count = 1
intNum = int(num)

while count < numLen:
    digit = num[:count]
    print(digit)
    count +1