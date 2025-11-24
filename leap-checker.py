while True:
    year = int(input("Enter a Year: "))
    if (year%4==0) or (year%400 ==0 and year%100 != 0):
        print(f"{year} is a Leap Year")
    else:
        print(f"{year} is not a Leap Year")
    cont = input("Do You want to continue?(y/n): ").strip().lower()
    if cont !="y":
        print("Program Closed")
        break