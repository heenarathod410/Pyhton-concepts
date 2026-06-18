import pandas as pd

df = pd.read_csv(r'D:\Python programing\Pandas\year-past.csv')  # to read a CSV file named 'data.csv' into a DataFrame
print("csv file read successfully!")  # to print a message confirming that the CSV file has been read successfully
print(df)  # to print the DataFrame
print("csv file head:")
print(df.head())  # to print the first 5 rows of the DataFrame
print("csv file tail:")
print(df.tail())  # to print the last 5 rows of the DataFrame
print("csv file columns:")
print(df.columns)  # to print the column names of the DataFrame
print("csv file info:")
print(df.info())  # to print the summary information about the DataFrame
print("csv file description:")
print(df.describe())  # to print the statistical summary of the DataFrame
print("csv file shape:")
print(df.shape)  # to print the number of rows and columns in the DataFrame

print("csv file missing values:")
print(df.isnull().sum())  # to print the number of missing values in each column of the DataFrame

print("csv file filled missing values:")
print(df.fillna(1999))  # to fill the missing values in the DataFrame with 0 and print the resulting DataFrame

print("csv file missing values:")
print(df.isnull().sum())

print("csv file dropped missing values:")
print(df.dropna())  # to drop the rows with missing values from the DataFrame and print the resulting DataFrame

df['date'] = pd.to_datetime(df['date'])

