# Python List1: Medical Insurance Project
# In this project, I will examine how factors such as age, sex, BMI, number of children, and smoking status contribute to medical insurance costs.
# By Anson Chow, 08/10/22

# Function to estimate insurance cost:
def estimate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):
  estimated_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
  print(name + "'s Estimated Insurance Cost: " + str(estimated_cost) + " dollars.")
  return estimated_cost
 
# Estimate Maria's insurance cost
maria_insurance_cost = estimate_insurance_cost(name = "Maria", age = 31, sex = 0, bmi = 23.1, num_of_children = 1, smoker = 0)

# Estimate Rohan's insurance cost
rohan_insurance_cost = estimate_insurance_cost(name = 
"Rohan", age = 25, sex = 1, bmi = 28.5, num_of_children = 3, smoker = 0)

# Estimate Valentina's insurance cost
valentina_insurance_cost = estimate_insurance_cost(name = "Valentina", age = 53, sex = 0, bmi = 31.4, num_of_children = 0, smoker = 1)

# Using Python Lists to store insurance cost data in a list as well as compare estimated insurance costs to actual insurance costs
names = ["Maria", "Rohan", "Valentina"]
insurance_costs = [4150.0, 5320.0, 35210.0]
insurance_data = list(zip(names, insurance_costs))
print("Here is the actual insurance cost data: " + str(insurance_data))

estimated_insurance_data = []
estimated_insurance_data.extend([("Maria", maria_insurance_cost), ("Rohan", rohan_insurance_cost), ("Valentina", valentina_insurance_cost)])
print("Here is the estimated insurance cost data: " + str(estimated_insurance_data))

#Calculate the difference between the actual insurance cost data and the estimated insurance cost data for each individual
Maira_cost_difference = insurance_data[0][1] - estimated_insurance_data[0][1]
print("The difference between the actual insurance cost data and the estimated insurance cost data for Maira is " + str(Maira_cost_difference) + " dollars")

Rohan_cost_difference = insurance_data[1][1] - estimated_insurance_data[1][1]
print("The difference between the actual insurance cost data and the estimated insurance cost data for Rohan is " + str(Rohan_cost_difference) + " dollars")

Valentina_cost_difference = insurance_data[2][1] - estimated_insurance_data[2][1]
print("The difference between the actual insurance cost data and the estimated insurance cost data for Valentina is " + str(Valentina_cost_difference) + " dollars")

# Estimate Akira's insurance cost & cost difference
Akira_insurance_cost = estimate_insurance_cost(name = "Akira", age = 19, sex = 1, bmi = 27.1, num_of_children = 0, smoker = 0)
insurance_data.append(("Akira", 2930.0))
estimated_insurance_data.append(("Akira", Akira_insurance_cost))

Akira_cost_difference = insurance_data[3][1] - estimated_insurance_data[3][1]
print("The difference between the actual insurance cost data and the estimated insurance cost data for Akira is " + str(Akira_cost_difference) + " dollars")