# Python Control Flow: Medical Insurance Project
# In this project, you will examine how factors such as age, sex, BMI, number of children, and smoking status contribute to medical insurance costs.
# By Anson Chow, 07/10/22

# Function to analyze Smoker Status:
def analyze_smoker(smoker_status):
  if smoker_status == 1:
    print("To lower your cost, you should consider quitting smoking.")
  else:
    print("Smoking is not an issue for you.")
  return smoker_status

# Function to analyze BMI:
def analyze_bmi(bmi_value):
  if bmi_value > 30:
    print("Your BMI is in the obese range. To lower your cost, you should significantly lower your BMI at least "
    + str(round(bmi_value-25, 1)) + " to bring it to a normal weight range.")
  elif bmi_value >= 25 and bmi_value <= 30:
    print("Your BMI is in the overweight range. To lower your cost, you should lower your BMI at least "
    + str(round(bmi_value-25, 1)) + " to bring it to a normal weight range.")
  elif bmi_value >= 18.5 and bmi_value < 25:
    print("Your BMI is in a healthy range.")
  else:
    print("Your BMI is in the underweight range. Increasing your BMI will not help lower your cost, but it will help improve your health. You should increase your BMI at least "
    + str(round(18 - bmi_value, 2)) + " to bring it to a normal weight range.")
  return bmi_value

# Function to estimate insurance cost:
def estimate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):
  estimated_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
  print(name + "'s Estimated Insurance Cost: " + str(round(estimated_cost, 1)) + " dollars.")
  analyze_smoker(smoker)
  analyze_bmi(bmi)
  return estimated_cost

# Estimate Keanu's insurance cost
keanu_insurance_cost = estimate_insurance_cost(
    name = 'Keanu', age = 29, sex = 1, bmi =26.2, num_of_children = 3, smoker = 1
    )

# Estimate Anson's insurance cost
Anson_insurance_cost = estimate_insurance_cost(
    name = 'Anson', age = 26, sex = 1, bmi =22.72, num_of_children = 0, smoker = 0
    )