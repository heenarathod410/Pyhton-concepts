import pandas as pd

# creating a serie
mydataset = {
    'cars': ["BMW", "Volvo", "Ford"],
    'passings': [3, 7, 2]
}

df = pd.DataFrame(mydataset)
print("==========================DataFrame:=================================")
print(df)

# creating a series from a list
a = [1, 7, 2]
myvar = pd.Series(a)
print("==========================creating a series from a list:=================================")
print(myvar)

# checking version of pandas
print(pd.__version__)

# creating a series from a dictionary
calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories)
print(myvar)

# creating a series from a list with index
calories = [420, 380, 390]
myvar = pd.Series(calories, index=["day1", "day2", "day3"])
print("==========================creating a series from a list with index:=================================")
print(myvar)

# Locate row
print("==========================Locate row:=================================")
print(df.loc[0] )

# Named Indexes
df = pd.DataFrame(mydataset, index = ["day1", "day2", "day3"])
print("==========================Named Indexes:=================================")
print(df)

# to read a csv file
df = pd.read_csv(r'D:\Python programing\Pandas\customers-1000.csv')
print("==========================Reading CSV file:=================================")
print(df)

df = pd.read_csv(r'D:\Python programing\Pandas\customers-1000.csv', nrows=5)
print("==========================First 5 rows:=================================")
print(df)

# df = pd.read_csv(r'D:\Python programing\Pandas\customers-1000.csv', usecols=['CustomerName', 'City'])
# print(df)

# df = pd.read_csv(r'D:\Python programing\Pandas\customers-1000.csv', usecols=['CustomerName', 'City'], nrows=5)
# print(df)

# df = pd.read_csv(r'D:\Python programing\Pandas\customers-1000.csv', usecols=['CustomerName', 'City'], nrows=5, index_col='CustomerName')
# print(df)

# df = pd.read_csv(r'D:\Python programing\Pandas\customers-1000.csv', usecols=['CustomerName', 'City'], nrows=5, index_col='CustomerName')
# print(df.loc['Alfreds Futterkiste'])

df = pd.read_csv(r'D:\Python programing\Pandas\customers-2000000.csv')
# print(df.to_string())

# to read only the first 5 rows of the file
df = pd.read_csv(r'D:\Python programing\Pandas\customers-2000000.csv', nrows=5)
print("==========================First 5 rows:=================================")
print(df.to_string())

# to read only the first 5 rows of the file and only the columns 'First Name' and 'City'
df = pd.read_csv(r'D:\Python programing\Pandas\customers-2000000.csv', usecols=['First Name', 'City'], nrows=5)
print("==========================First 5 rows with specific columns:=================================")
print(df.to_string())

# to read only the first 5 rows of the file and only the columns 'First Name' and 'City' and set the index to 'First Name'
df = pd.read_csv(r'D:\Python programing\Pandas\customers-2000000.csv', usecols=['First Name', 'City'], nrows=5, index_col='First Name')
print("==========================First 5 rows with specific columns and named index:=================================")
print(df.to_string())

# to read only the first 5 rows of the file and only the columns 'First Name' and 'City' and set the index to 'First Name' and locate the row with index 'Maria'
df = pd.read_csv(r'D:\Python programing\Pandas\customers-2000000.csv', usecols=['First Name', 'City'], nrows=5, index_col='First Name')
print(df.loc['Arthur'])

# to read only the first 5 rows of the file and only the columns 'First Name', 'City', 'Country', 'Company' and 'Email' and set the index to 'First Name' and locate the row with index 'Maria'
df = pd.read_csv(r'D:\Python programing\Pandas\customers-2000000.csv', usecols=['First Name', 'City', 'Country', 'Company', 'Email'], nrows=5, index_col='First Name')
print
print(df.loc['Arthur'])

# to read the file and only the column 'Country' and filter the rows where the value in the 'Country' column is 'India'
df = pd.read_csv(r'D:\Python programing\Pandas\customers-2000000.csv', usecols=['Country'])
india_df = df[df['Country'] == 'India']
print("==========================Rows where Country is India:=================================")
print(india_df)
print(india_df.sum())

# to read the file and skip the first row
df = pd.read_csv(r'D:\Python programing\Pandas\customers-1000.csv', skiprows=1) 
print("==========================Skipping the first row:=================================")
print(df)

# to read the file and skip the first 5 rows
df = pd.read_csv(r'D:\Python programing\Pandas\customers-1000.csv', skiprows=5)
print("==========================Skipping the first 5 rows:=================================")
print(df)


df = pd.read_csv(r'D:\Python programing\Pandas\customers-1000.csv')
print("==========================First 10 rows:=================================")
print(df.head(10))  # to read the first 10 rows of the file

df = pd.read_csv(r'D:\Python programing\Pandas\customers-1000.csv')
print("==========================Last 10 rows:=================================")
print(df.tail(10))  # to read the last 10 rows of the file

df = pd.read_csv(r'D:\Python programing\Pandas\customers-1000.csv')
print("==========================File Information:=================================")
print(df.info())  # to get information about the file

df = pd.read_csv(r'D:\Python programing\Pandas\customers-1000.csv')
print(df.describe())  # to get statistical information about the file

df = pd.read_csv(r'D:\Python programing\Pandas\customers-1000.csv')
print("==========================Column Names:=================================")
print(df.columns)  # to get the column names of the file

df = pd.read_csv(r'D:\Python programing\Pandas\customers-1000.csv')
print("==========================Data Types:=================================")
print(df.dtypes)  # to get the data types of the columns in the file

df = pd.read_csv(r'D:\Python programing\Pandas\customers-1000.csv')
print("==========================Shape:=================================")
print(df.shape)  # to get the number of rows and columns in the file

df = pd.read_csv(r'D:\Python programing\Pandas\customers-1000.csv')
print("==========================Size:=================================")
print(df.size)  # to get the number of elements in the file

df = pd.read_csv(r'D:\Python programing\Pandas\customers-1000.csv')
print("==========================Null Values:=================================")
print(df.isnull())  # to check for null values in the file

df = pd.read_csv(r'D:\Python programing\Pandas\customers-1000.csv')
print("==========================Number of Null Values:=================================")
print(df.isnull().sum())  # to get the number of null values in each column

df = pd.read_csv(r'D:\Python programing\Pandas\customers-1000.csv')
print("==========================Non-Null Values:=================================")
print(df.notnull())  # to check for non-null values in the file

df = pd.read_csv(r'D:\Python programing\Pandas\customers-1000.csv')
print("==========================Number of Non-Null Values:=================================")
print(df.notnull().sum())  # to get the number of non-null values in each

df = pd.read_csv(r'D:\Python programing\Pandas\customers-1000.csv')
print("==========================Correlation:=================================")
print(df.corr(method='pearson', numeric_only=True).round(2))  # to get the correlation between the columns in the file


df = pd.read_csv(r'D:\Python programing\Pandas\customers-1000.csv')
print("==========================Correlation using Pearson method:=================================")
print(df.corr(method='pearson', numeric_only=True))  # to get the correlation between the columns in the file using the Pearson method

df = pd.read_csv(r'D:\Python programing\Pandas\customers-1000.csv')
print("==========================Correlation using Kendall method:=================================")
print(df.corr(method='kendall', numeric_only=True).round(2))  # to get the correlation between the columns in the file using the Kendall method

df = pd.read_csv(r'D:\Python programing\Pandas\customers-1000.csv')
print("==========================Correlation using Spearman method:=================================")
print(df.corr(method='spearman', numeric_only=True))  # to get the correlation between the columns in the file using the Spearman method

df = pd.read_csv(r'D:\Python programing\Pandas\customers-1000.csv')
print("==========================Correlation with Minimum Periods:=================================")
print(df.corr(method='pearson', min_periods=2,numeric_only=True).round(2))  # to get the correlation between the columns in the file using the Pearson method and setting the minimum number of observations to 1

df = pd.read_csv(r'D:\Python programing\Pandas\customers-1000.csv')
print("==========================Correlation with Minimum Periods:=================================")
print(df.corr(method='kendall', min_periods=2,numeric_only=True).round(2)) # to get the correlation between the columns in the file using the Kendall method and setting the minimum number of observations to 1

# df = pd.read_csv(r'D:\Python programing\Pandas\customers-1000.csv')
# print("==========================Correlation with Minimum Periods:=================================")
# print(df.corr(method='spearman', min_periods=2, numeric_only=True).round(2))  # to get the correlation between the columns in the file using the Spearman method and setting the minimum number of observations to 1    

df = pd.read_csv(r'D:\Python programing\Pandas\customers-1000.csv')
print("==========================Correlation with Numeric Only:=================================")
print(df.corr(method='pearson', min_periods=1, numeric_only=True))  # to get the correlation between the columns in the file using the Pearson method and setting the minimum number of observations to 1 and only considering numeric columns

df = pd.read_csv(r'D:\Python programing\Pandas\customers-1000.csv')
print("==========================Correlation with Numeric Only:=================================")
print(df.corr(method='kendall', min_periods=1, numeric_only=True))  # to get the correlation between the columns in the file using the Kendall method and setting the minimum number of observations to 1 and only considering numeric columns

df = pd.read_csv(r'D:\Python programing\Pandas\customers-1000.csv')
print("==========================Correlation with Numeric Only:=================================")
print(df.corr(method='spearman', min_periods=1, numeric_only=True))  # to get the correlation between the columns in the file using the Spearman method and setting the minimum number of observations to 1 and only considering numeric columns

df = pd.read_csv(r'D:\Python programing\Pandas\customers-1000.csv')
print("==========================Absolute Correlation:=================================")
print(df.corr(method='pearson', min_periods=1, numeric_only=True).abs())  # to get the absolute value of the correlation between the columns in the file using the Pearson method and setting the minimum number of observations to 1 and only considering numeric columns  

df = pd.read_csv(r'D:\Python programing\Pandas\customers-1000.csv')
print("==========================Absolute Correlation:=================================")
print(df.corr(method='kendall', min_periods=1, numeric_only=True).abs())  # to get the absolute value of the correlation between the columns in the file using the Kendall method and setting the minimum number of observations to 1 and only considering numeric columns

df = pd.read_csv(r'D:\Python programing\Pandas\customers-1000.csv')
print("==========================Absolute Correlation:=================================")
print(df.corr(method='spearman', min_periods=1, numeric_only=True).abs())  # to get the absolute value of the correlation between the columns in the file using the Spearman method and setting the minimum number of observations to 1 and only considering numeric columns

df = pd.read_csv(r'D:\Python programing\Pandas\customers-1000.csv')
print("==========================Absolute Correlation with Rounding:=================================")
print(df.corr(method='pearson', min_periods=1, numeric_only=True).abs().round(2))  # to get the absolute value of the correlation between the columns in the file using the Pearson method and setting the minimum number of observations to 1 and only considering numeric columns and rounding the result to 2 decimal places

df = pd.read_csv(r'D:\Python programing\Pandas\customers-1000.csv')
print("==========================Absolute Correlation with Rounding:=================================")
print(df.corr(method='kendall', min_periods=1, numeric_only=True).abs().round(2))  # to get the absolute value of the correlation between the columns in the file using the Kendall method and setting the minimum number of observations to 1 and only considering numeric columns and rounding the result to 2 decimal places

df = pd.read_csv(r'D:\Python programing\Pandas\customers-1000.csv')
print("==========================Absolute Correlation with Rounding:=================================")
print(df.corr(method='spearman', min_periods=1, numeric_only=True).abs().round(2))  # to get the absolute value of the correlation between the columns in the file using the Spearman method and setting the minimum number of observations to 1 and only considering numeric columns and rounding the result to 2 decimal places

df = pd.read_csv(r'D:\Python programing\Pandas\customers-1000.csv')
print("==========================Absolute Correlation with Rounding and Unstacking:=================================")
print(df.corr(method='pearson', min_periods=1, numeric_only=True).abs().round(2).unstack())  # to get the absolute value of the correlation between the columns in the file using the Pearson method and setting the minimum number of observations to 1 and only considering numeric columns and rounding the result to 2 decimal places and unstacking the result 

