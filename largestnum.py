while True:
    while True:  # Keep asking until correct input
        try:
            num1, num2, num3 = map(int, input("Enter 3 numbers separated by space: ").split())
            break  # exit inner loop if input is correct
        except ValueError:
            print("Invalid input! Please enter exactly three numbers separated by spaces.")

    # Find the largest using nested if-else
    if num1 >= num2:
        if num1 >= num3:
            largest = num1
        else:
            largest = num3
    else:
        if num2 >= num3:
            largest = num2
        else:
            largest = num3

    print(f"The largest number is: {largest}")

    cont = input("Do you want to continue? (y/n): ").lower()
    if cont != "y":
        print("Program Closed")
        break
