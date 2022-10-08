# Python Syntax: Medical Insurance Project
# In this project, I will investigate how different factors such as age, sex, BMI, etc. affect the prediction.
# By Anson Chow, 15/09/22

# create the initial variables below
age = 28
sex = 0
bmi = 26.2
num_of_children = 3
smoker = 0

# Add insurance estimate formula below
insurance_cost =250*age- 128*sex+370*bmi+425*num_of_children+24000*smoker- 12500
print("This person's insurance cost is " + str(insurance_cost) + " dollars.")

# Age Factor
age += 4
new_insurance_cost =250*age- 128*sex+370*bmi+425*num_of_children+24000*smoker- 12500
print(new_insurance_cost)

change_in_insurance_cost = new_insurance_cost - insurance_cost
print("The change in cost of insurance after increasing the age by 4 years is " + str(change_in_insurance_cost) + " dollars.")

# BMI Factor
age = 28
bmi += 3.1

new_insurance_cost =250*age- 128*sex+370*bmi+425*num_of_children+24000*smoker- 12500
print(new_insurance_cost)

change_in_insurance_cost = new_insurance_cost - insurance_cost
print("The change in estimated insurance cost after increasing BMI by 3.1 is " + str(change_in_insurance_cost) + " dollars.")

# Male vs. Female Factor
bmi = 26.2
sex = 1

new_insurance_cost =250*age- 128*sex+370*bmi+425*num_of_children+24000*smoker- 12500
print(new_insurance_cost)

change_in_insurance_cost = new_insurance_cost - insurance_cost
print("The change in estimated cost for being male instead of female is " + str(change_in_insurance_cost) + " dollars.")

sex = 0

# Smoker factor
smoker = 1

new_insurance_cost =250*age- 128*sex+370*bmi+425*num_of_children+24000*smoker- 12500
print(new_insurance_cost)

change_in_insurance_cost = new_insurance_cost - insurance_cost
print("The change in estimated cost for smoker instead of non-smoker is " + str(change_in_insurance_cost) + " dollars.")

smoker = 0

# Number of children factor
num_of_children += 1

new_insurance_cost =250*age- 128*sex+370*bmi+425*num_of_children+24000*smoker- 12500
print(new_insurance_cost)

change_in_insurance_cost = new_insurance_cost - insurance_cost
print("The change in estimated cost for one more children is " + str(change_in_insurance_cost) + " dollars.")