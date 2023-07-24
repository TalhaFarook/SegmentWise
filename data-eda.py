import matplotlib.pyplot as plot
import seaborn as sns
import pandas

customerData = pandas.read_csv("TechElectro_Customer_Data.csv")

# Plotting a histogram of Age distribution
plot.figure(figsize = (10, 6))

sns.histplot(customerData['Age'], bins = 20)

plot.xlabel('Age')
plot.ylabel('Frequency')
plot.title('Histogram of Age Distribution')

plot.show()

# Plotting a boxplot of Annual Income by Gender
plot.figure(figsize = (10, 6))

sns.boxplot(x = 'Gender', y = 'Annual Income', data = customerData)

plot.xlabel('Gender')
plot.ylabel('Annual Income')
plot.title('Box Plot of Annual Income by Gender')

plot.show()

# Plotting a countplot of Marital Status
plot.figure(figsize = (10, 6))

sns.countplot(x = 'Marital Status', data = customerData)

plot.xlabel('Marital Status')
plot.ylabel('Count')
plot.title('Count Plot of Marital Status Distribution')

plot.show()

# Plotting a scatter plot of Age & Total Purchases with hue showing the gender associated to each plot
plot.figure(figsize = (10, 6))

sns.scatterplot(x = 'Age', y = 'Total Purchases', data = customerData, hue = 'Gender')

plot.xlabel('Age')
plot.ylabel('Total Purchases')
plot.title('Scatter Plot of Age & Total Purchases w/ Hue of Gender')
plot.show()

# Plotting a bar plot of Preferred Category distribution
plot.figure(figsize = (10, 6))

sns.countplot(x = 'Preferred Category', data = customerData)

plot.xlabel('Preferred Category')
plot.ylabel('Count')
plot.title('Bar Plot of Preferred Category Distribution')

plot.show()

# Plotting a pairplot to visualize relationships between numerical variables
plot.figure(figsize = (10, 6))

sns.pairplot(customerData[['Age', 'Annual Income', 'Total Purchases']], diag_kind='kde')
plot.suptitle("Pair Plot between Age, Annual Income & Total Purchases", y = 1.05)

plot.show()

# Plotting a correlation heatmap of numerical variables
plot.figure(figsize = (10, 6))

sns.heatmap(customerData[['Age', 'Annual Income', 'Total Purchases']].corr(), annot = True, cmap = 'coolwarm')

plot.title('Correlation Heatmap of Age, Annual Income & Total Purchases')

plot.show()

# Plotting a box plot of Marital Status and Annual Income w/ Hue showing the gender associated with it
plot.figure(figsize = (10, 6))

sns.boxplot(x = 'Marital Status', y = 'Annual Income', hue = 'Gender', data = customerData)

plot.xlabel('Marital Status')
plot.ylabel('Annual Income')
plot.title('Annual Income by Marital Status and Gender')
plot.legend(title='Gender', loc='lower right')

plot.show()

# Plotting a violin plot of Age distribution by Preferred Category
plot.figure(figsize = (10, 6))

sns.violinplot(x = 'Preferred Category', y = 'Age', data = customerData)

plot.xlabel('Preferred Category')
plot.ylabel('Age')
plot.title('Violin Plot of Age Distribution by Preferred Category')

plot.show()