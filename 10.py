#Write a Python program to find the greatest number among n numbers.
numbers = list( map(int,input("Enter Your Numbers Separated by space: ").split()))
greatest = max(numbers)
print(f"{greatest} is the greatest number")
