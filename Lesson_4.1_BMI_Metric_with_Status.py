#--- Gathering
weight = float(input("Please enter weight in kilograms: "))
height = float(input("Please enter height in meters: "))

#--- Converting
#weight = float(weight * 0.453592)
#height = float(height * 0.0254)

#--- Calculating
bmi = weight/(height**2)

#--- Assigning Category
if (0 < bmi < 18.5):
    print("BMI is: ", "%.2f"%bmi,", Status is Underweight", sep="")
elif (18.5 <= bmi <= 24.9):
    print("BMI is: ", "%.2f"%bmi,", Status is Normal", sep="")
elif (25 <= bmi <= 29.9):
    print("BMI is: ", "%.2f"%bmi,", Status is Overweight", sep="")
elif (30 <= bmi):
    print("BMI is: ", "%.2f"%bmi,", Status is Obese", sep="")
elif ():
    print("Not a valid input.")
