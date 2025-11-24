while True:
    string = input("Enter your string: ").strip()
    convTo = input("Convert to (uppercase/lowercase): ").strip().lower()

    if convTo == "uppercase":
        print(f"Converted: {string.upper()}")
    elif convTo == "lowercase":
        print(f"Converted: {string.lower()}")
    else:
        print("Invalid choice! Please enter 'uppercase' or 'lowercase'.")

    cont = input("\nDo you want to continue? (yes/no): ").strip().lower()
    if cont != "yes":
        print("Program closed.")
        break
