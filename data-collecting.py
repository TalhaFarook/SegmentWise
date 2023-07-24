import pandas
import random

# Creating a custom dataset using random function of 1000 instances.
customerData = []
for id in range(1000, 2000):
    temp = []
    temp.append(id) 
    temp.append(random.randint(19, 75)) # Age
    temp.append(random.choice(["Male", "Female"])) # Gender
    temp.append(random.choice(["Married", "Single", "Divorced"])) # Marital Status
    temp.append(random.randint(15, 95) * 1000) # Annual Income
    temp.append(random.randint(1, 70)) # Total Purchases
    temp.append(random.choice(["Electronics", "Appliances"])) # Preferred Category
    customerData.append(temp)
    
customerData = pandas.DataFrame(customerData, columns = ['Customer ID', 'Age', 'Gender', 'Marital Status', 'Annual Income', 'Total Purchases', 'Preferred Category'])
customerData.to_csv("TechElectro_Customer_Data.csv", index=False)

customerData = pandas.read_csv('TechElectro_Customer_Data.csv')
print(customerData)