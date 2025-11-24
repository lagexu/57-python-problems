while True:
    num = int(input("Enter Your Number: "))

    if num == 0:
        print("Given Value is 0")
    elif num % 2 == 0:
        print(f"{num} is an Even Number")
    else:
        print(f"{num} is an Odd Number")

    cont = input("Do You Want to Continue? (yes/no): ").lower()

    if cont != "yes":
        print("Program Closed")
        break
