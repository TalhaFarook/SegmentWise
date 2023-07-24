import pandas
from sklearn.cluster import KMeans
model = KMeans(n_clusters = 3, random_state = 0)

customerData = pandas.read_csv("TechElectro_Customer_Data_Preprocessed.csv")

customerData['Cluster'] = model.fit_predict(customerData)

customerData.to_csv("TechElectro_Customer_Data_Clustered.csv", index = False)