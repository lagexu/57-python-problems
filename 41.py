#Write a Python program to calculate simple interest given the principle,rate of interest, and time.
p = float(input("Enter Principal Amount: "))
r = float(input("Enter Rate of Interest: "))
t = float(input("Enter Time (in years): "))

simple_interest = (p * r * t) / 100

print("Simple Interest =", simple_interest)
