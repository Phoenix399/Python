#Python weight converter

weight = float(input("Enter your weight "))
unit = input("Enter the unit (kg or lb): ")

if unit.lower() == "kg":
    converted_weight = weight * 2.20462
    print(f"Your weight in pounds is: {converted_weight:.2f} lb")
elif unit.lower() == "lb":
    converted_weight = weight / 2.20462
    print(f"Your weight in kilograms is: {converted_weight:.2f} kg")
else:
    print("Invalid unit.")