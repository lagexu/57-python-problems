# Write a Python Program to convert a temperature from Celsius to Fahrenheit and Kelvin.

temp = float(input("Enter Your Temperature in Celsius: "))
tempInFahrenheit= (temp*1.8)+32
tempInKelvin = temp+273.15
print(f"{temp}°C = {tempInFahrenheit}°F")
print(f"{temp}°C = {tempInKelvin}°K")

    