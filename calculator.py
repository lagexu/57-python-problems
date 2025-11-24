while True:
    firstNum = int(input("Enter Your First Number: "))
    secondNum = int(input("Enter Your Second Number: "))
    operation = input("Enter Your Operation ( +, -, *, /): ")
    match operation:
        case '+':
            print(f"Result: {firstNum+secondNum}")
        case '-':
            print(f"Result: {firstNum-secondNum}")
        case '*':
            print(f"Result: {firstNum*secondNum}")
        case '/':
            print(f"Result: {firstNum/secondNum}")
        case _:
            print(f"Unknown Operation: {operation}")
    cont = input("Do you want to continue?: (yes/no) ").strip().lower()
    if(cont != "yes"):
        print("Calculator Closed")
        break
    
    