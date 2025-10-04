unit = input("Enter the unit in Celsius or Fahrenheit (C or F): ")
temperature = float(input("Enter the temperature: "))

if unit.upper() == "C":
    fahrenheit = (temperature * 9/5) + 32
    print(f"{temperature}°C is {fahrenheit:.2f}°F")

elif unit.upper() == "F":
    celsius = (temperature - 32) * 5/9
    print(f"{temperature}°F is {celsius:.2f}°C")

else:
    print("Invalid unit. Please enter 'C' or 'F'.")
