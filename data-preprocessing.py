import pandas

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()

from sklearn.preprocessing import OrdinalEncoder
encoder = OrdinalEncoder()

customerData = pandas.read_csv("TechElectro_Customer_Data.csv")
# No missing values will be present, because these values were randomly producted. But, duplicate values may exist, so checking for them.

print("Null:", customerData.isna().sum().sum())
#No null values found!

print("Duplicates:", customerData.duplicated().sum())
# No duplicates found!

# I will be applying clustering algorithms (e.g., K-means) to this dataset, so some pre-processing steps are necessary.

# K-means is sensitive to the scale of features, so it's essential to apply feature scaling to numerical columns. In this case, the numerical columns are "Age", "AnnualIncome", and "TotalPurchases". Applying Min-Max Scaling on these columns.
numerical = ['Age', 'Annual Income', 'Total Purchases']
customerData[numerical] = scaler.fit_transform(customerData[numerical])

# K-means algorithm cannot directly handle categorical variables, so I will need to encode them into numerical representations. For the "Gender", "MaritalStatus" and "Preferred Category" columns, I will use label encoding, which maps each category to a unique integer.
categorical = ['Gender', 'Marital Status', 'Preferred Category']
customerData[categorical] = encoder.fit_transform(customerData[categorical])

# Preproccesed dataset 
customerData.to_csv("TechElectro_Customer_Data_Preprocessed.csv", index = False)