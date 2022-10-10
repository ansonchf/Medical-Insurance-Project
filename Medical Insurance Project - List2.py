# Python List2: Medical Insurance Project
# In this project, I will store medical data and see what valuable insights you can gain from that data.
# By Anson Chow, 10/10/22

names = ["Mohamed", "Sara", "Xia", "Paul", "Valentina", "Jide", "Aaron", "Emily", "Nikita", "Paul"]
insurance_costs = [13262.0, 4816.0, 6839.0, 5054.0, 14724.0, 5360.0, 7640.0, 6072.0, 2750.0, 12064.0]

# Add additional data and group the list
names.append("Priscilla")
insurance_costs.append(8320.0)
medical_records = list(zip(insurance_costs, names))

# Number of medical records 
num_medical_records = len(medical_records)
print("There are " + str(num_medical_records) + " medical records.")

# The first medical record
first_medical_record = medical_records[0]
print("Here is the first medical record: " + str(first_medical_record))

# Sort by lowest insurance costs
medical_records = sorted(medical_records)
print("Here are the medical records sorted by insurance cost: " + str(medical_records))

# Three cheapest insurance costs
cheapest_three = medical_records[:3]
print("Here are the three cheapest insurance costs in our medical records: " + str(cheapest_three))

# Three mose expensive insurance costs
priciest_three = medical_records[-3:]
print("Here are the three most expensive insurance costs in our medical records: " + str(priciest_three))

# Count the number of occurrences of “Paul” in the list
occurrences_paul = names.count("Paul")
print("There are " + str(occurrences_paul) + " individuals with the name Paul in our medical records. ")

# Sort the medical records alphabetically by name
new_medical_records = list(zip(names, insurance_costs))
new_medical_records = sorted(new_medical_records)
print(new_medical_records)

# Select the medical records starting at index 3 and ending at index 7
middle_five_records = medical_records[3:8]
print(middle_five_records)