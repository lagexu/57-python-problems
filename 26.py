#Write a Python program to create a list,add elements to it, and print the list.
my_list = []

while True:
    print("\n1. Create a List\n2. Add Elements\n3. Show List")
    userInput = input("Choose an option (1|2|3): ").strip()
    
    if userInput == "1":
        my_list = []
        print("List Created Successfully ✅")
    elif userInput == "2":
        element = input("Enter element to add: ").strip()
        my_list.append(element)
        print(f"'{element}' added to the list.")
    elif userInput == "3":
        print("Current List:", my_list)
    else:
        print("Invalid Input! ❌")
    
    cont = input("Do you want to continue? (y/n): ").lower()
    if cont != "y":
        break
