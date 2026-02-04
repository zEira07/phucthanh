inches = float(input("Enter inches: "))

while inches >= 0:
    centimeters = inches * 2.54
    print(f"{inches} inches = {centimeters:.2f} cm")
    inches = float(input("Enter inches: "))

print("Program ended.")
