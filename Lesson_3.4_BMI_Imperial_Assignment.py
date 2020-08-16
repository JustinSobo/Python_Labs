weight = float(input("Please enter weight in pounds: "))
height = float(input("Please enter height in inches: "))

weight = float(weight * 0.453592)
height = float(height * 0.0254)

print("BMI is:", weight/height**2)
