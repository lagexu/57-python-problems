# Write a Python Program  to convert a given string to upppercase and lowercase.
string = input("Enter your string: ").strip()
convTo = input("Convert to (uppercase/lowercase): ").strip().lower()
if convTo == "uppercase":
    print(f"Converted: {string.upper()}")
elif convTo == "lowercase":
    print(f"Converted: {string.lower()}")
else:
    print("Invalid choice! Please enter 'uppercase' or 'lowercase'.")


