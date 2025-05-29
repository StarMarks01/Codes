def calculate_bmi(weight, height):
  bmi = weight / (height * height)
  return bmi

def classify_bmi(bmi):
  if bmi < 18.5:
      return "Underweight"
  elif bmi < 25:
      return "Normal weight"
  elif bmi < 30:
      return "Overweight"
  else:
      return "Obese"

a="Welcome to the BMI Calculator!"
print(a.center(100))
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

bmi = calculate_bmi(weight, height)
print("Your BMI is:", bmi)
print("")

classification = classify_bmi(bmi)
print("You are classified as:", classification)
print("")

if classification == "Underweight":
  c='''you shold focous on srength training to build mucle mass and increase your calorie intake
  you shold add this food items in your diet for weight gain:
    >  Nuts and Nut Butters
    >  Avocado
    >  Quinoa
    >  Tahini
    >  Olive oil
    >  Dried Fruit
    >  Legumes
    >  Sweet Potatoes'''
elif classification == "Obese":
  c='''you shold focous on cardio for weight loss
  you shold add this food items in your diet for weight loss:
    >  Lentils (Dal) 
    >  Chickpeas (Chana) 
    >  Amaranth And Quinoa.
    >  Spinach
    >  Almonds
    >  Paneer Or Cottage Cheese
    >  Broccoli
  '''
elif classification == "Overweight":
  c='''you shold focous on cardio for weight loss
  you shold add this food items in your diet for weight loss:
    >  Lentils (Dal) 
    >  Chickpeas (Chana) 
    >  Amaranth And Quinoa.
    >  Spinach
    >  Almonds
    >  Paneer Or Cottage Cheese
    >  Broccoli
'''
else:
  c='''you shold focous on building muscle by strenght training and also do cardio 
       you shold add this food items in your diet for muscle buildy:
    >  Paneer
    >  Greek yogurt
    >  Nuts
    >  Leafy greens
    >  Cruciferous vegetables
    > Quinoa
    >  Milk
    >  Beans 
    > legumes'''
print("")
print(c)
print("")
print("stay healthy :)")