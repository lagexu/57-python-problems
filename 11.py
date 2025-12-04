#Write a Python Program to assign a letter grade (A,B,C,D,E,F) based on a students score.

mark = int(input("Enter Your Mark: "))
if mark>=90 and mark<=100:
    print("You got A")
elif mark>=80 and mark<=89:
    print("You got B")
elif mark>=70 and mark<=79:
    print("You got C")
elif mark>=60 and mark<=69:
    print("You got D")
elif mark>=50 and mark<=59:
    print("You got E")
elif mark>=0 and mark<=49:
    print("You got F")
else:
    print("Enter Valid Number")