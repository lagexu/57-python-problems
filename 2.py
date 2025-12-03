#Write a Python Program to create a simple calculator that can perform addition,subtraction,multiplication, and division.

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

    
    