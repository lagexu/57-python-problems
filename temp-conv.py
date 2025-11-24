while True:
    temp = float(input("Enter Your Temperature in Celsius: "))
    tempInFahrenheit= (temp*1.8)+32
    tempInKelvin = temp+273.15
    print(f"{temp}°C = {tempInFahrenheit}°F")
    print(f"{temp}°C = {tempInKelvin}°K")
    cont = input("Do You Want to Continue?:(yes/no) ").strip().lower()
    if(cont!="yes"):
        print("Program Closed!")
        break
   