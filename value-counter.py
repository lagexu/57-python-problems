while True:
    string = input("Enter your string: ")
    value = input("Enter the value you want to count: ")

    count = string.count(value)
    print(f"'{value}' appears {count} time(s) in the string.")

    cont = input("Do you want to continue? (yes/no): ").strip().lower()
    if cont != "yes":
        print("Program closed.")
        break
