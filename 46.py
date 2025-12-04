#Write a Python program  to print all prime numbers up to specified number using nested loops.

till = int(input("Enter the upper limit: "))

print(f"Prime numbers up to {till} are:")

for num in range(2, till + 1):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)
