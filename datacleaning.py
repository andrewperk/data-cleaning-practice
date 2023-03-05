medical_data = \
"""Marina Allison   ,27   ,   31.1 , 
#7010.0   ;Markus Valdez   ,   30, 
22.4,   #4050.0 ;Connie Ballard ,43 
,   25.3 , #12060.0 ;Darnell Weber   
,   35   , 20.6   , #7500.0;
Sylvie Charles   ,22, 22.1 
,#3022.0   ;   Vinay Padilla,24,   
26.9 ,#4620.0 ;Meredith Santiago, 51   , 
29.3 ,#16330.0;   Andre Mccarty, 
19,22.7 , #2900.0 ; 
Lorena Hodson ,65, 33.1 , #19370.0; 
Isaac Vu ,34, 24.8,   #7045.0"""

# The initial medical data to clean
print(medical_data)
print("----")

# Replace pound with dollar sign
updated_medical_data = medical_data.replace("#", "$")
print(updated_medical_data)
print("----")

# Get total number of medical records
num_records = 0
for i in range(0, len(updated_medical_data)):
  if updated_medical_data[i] == "$":
    num_records += 1
print(num_records)
print("----")

# Split data by semicolon
medical_data_split = updated_medical_data.split(";")
print(medical_data_split)
print("----")

# Split eeach record by comma
medical_records = []
for data in medical_data_split:
  medical_records.append(data.split(","))
print(medical_records)
print("----")

# Strip the leading and trailing spaces
medical_records_clean = []
for data in medical_records:
  record_clean = []
  for item in data:
    record_clean.append(item.strip())
  medical_records_clean.append(record_clean)
print(medical_records_clean)
print("----")

# Display names in uppercase
for record in medical_records_clean:
  record[0] = record[0].upper()
  print(record[0])
print("----")

# lists for each data of the record
names = []
ages = []
bmis = []
insurance_costs = []

# loop through records to make separate lists for each data
for record in medical_records_clean:
  names.append(record[0])
  ages.append(record[1])
  bmis.append(record[2])
  insurance_costs.append(record[3])

print(names)
print(ages)
print(bmis)
print(insurance_costs)
print("----")

# calculate total bmi
total_bmi = 0
for bmi in bmis:
  total_bmi += float(bmi)

# calculate average bmi
average_bmi = total_bmi/len(bmis)
print("Average BMI: {}".format(average_bmi))
print("----")

#calculate average insurance costs
total_insurance_costs = 0
for cost in insurance_costs:
  total_insurance_costs += float(cost.replace("$", ""))
average_insurance_costs = total_insurance_costs/len(insurance_costs)
print("Average insurance costs: {}".format(average_insurance_costs))
print("----")

# Display custom message about each record
for i in range(0, len(medical_records_clean)):
  print("{} is {} years old with a BMI of {} and an insurance cost of {}".format(names[i], ages[i], bmis[i], insurance_costs[i]))