while True:
    numbers = list( map(int,input("Enter Your Numbers Separated by space: ").split()))
    greatest = numbers[0]
    for num in numbers:
        if num > greatest:
            greatest = num
    print(f"{greatest} is the greatest number")

    cont = input("Do you want to continue? (y/n): ").lower()
    if cont != "y":
        print("Program Closed")
        break