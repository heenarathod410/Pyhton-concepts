import pandas as pd

df = pd.read_csv(r'D:\Python programing\Pandas\sales.csv')  # to read a CSV file named 'data.csv' into a DataFrame
print("csv file read successfully!")  # to print a message confirming that the CSV file has been read successfully
print(df)  # to print the DataFrame

# Level 1: Basic Business Questions
# Q1: total Revenue & total profit
total_revenue = df['Sales'].sum()
total_profit = (df['Sales'] - df['Cost']).sum()
print("\nTotal Revenue:", total_revenue)
print("Total Profit:", total_profit)
# 🔥 Upgrade (Cleaner + reusable)
# You already created Profit later—use it here:
df['Profit'] = df['Sales'] - df['Cost']
total_profit = df['Profit'].sum()
print("\nTotal Profit (using Profit column):", total_profit)


# Q2: profit per city
# which city performing well?
profit_per_city = df.groupby('City')['Sales'].sum() - df.groupby('City')['Cost'].sum()
print("\nProfit per City:")
print(profit_per_city)
# ❗ But not ideal (repeating groupby twice)
# ✅ Better Version
# profit_per_city = df.groupby('City')['Profit'].sum()

# Q3: top 3 customers by profit
# who are our best customers?
df['Profit'] = df['Sales'] - df['Cost']  # to add a new column 'Profit' to the DataFrame by calculating the difference between Sales and Cost
profit_per_customer = df.groupby('Customer')['Profit'].sum()  # to calculate the total profit for each customer by grouping the DataFrame by 'Customer' and summing the 'Profit' column
top_3_customers = profit_per_customer.nlargest(3)  # to get the top 3 customers by profit
print("\nTop 3 Customers by Profit:")
print(top_3_customers)  # to print the total profit for each customer
# 🔥 Upgrade (More practical output)
# df.nlargest(3, 'Profit')[['Customer', 'Profit']]

# Q4: loss detection
# are we losing money on any customer?
loss_per_customer = df.groupby('Customer')['Profit'].sum()  # to calculate the total profit for each customer by grouping the DataFrame by 'Customer' and summing the 'Profit' column
customers_with_loss = loss_per_customer[loss_per_customer < 0]  # to filter the customers who are losing money by selecting the rows where the total profit is less than 0
print("\nCustomers with Loss:")
print(customers_with_loss)  # to print the customers who are losing money
# ✅ Simpler Version
# df[df['Profit'] < 0]


# level 2: Decision Making 
# Q5: high value customers
# find customer 
# sales > 1500
# And profit > 500
high_value_customers = df[(df['Sales'] > 1500) & (df['Profit'] > 500)]['Customer'].unique()  # to filter the customers who are high value by selecting the rows where Sales is greater than 1500 and Profit is greater than 500, and then getting the unique customer names
print("\nHigh Value Customers:")
print(high_value_customers)  # to print the high value customers
# 🔥 Upgrade (Better output)
# df[(df['Sales'] > 1500) & (df['Profit'] > 500)][['Customer', 'Sales', 'Profit']]

# Q6:city performance category
# create column new column
# profit >= 2000 -> Excellent
# profit >= 1000 and < 2000 -> Good
# profit < 1000 -> Poor
def performance_category(profit):
    if profit >= 2000:
        return 'Excellent'
    elif profit >= 1000 and profit < 2000:
        return 'Good'
    else:
        return 'Needs Improvement'
# ✅ Correct Business Thinking
# city_profit = df.groupby('City')['Profit'].sum()  # to calculate the total profit for each city by grouping the DataFrame by 'City' and summing the 'Profit' column
df['Performance Category'] = df['Profit'].apply(performance_category)  # to create a new column 'Performance Category' in the DataFrame by applying the performance_category function to the 'Profit' column
print("\nDataFrame with Performance Category:")
print(df)  # to print the DataFrame with the new 'Performance Category' column

# Q7: best city
# which city has the highest total profit?
best_city = df.groupby('City')['Profit'].sum().idxmax()  # to find the city with the highest total profit by grouping the DataFrame by 'City', summing the 'Profit' column for each city, and then getting the index of the maximum value
print("\nBest Performing City:", best_city)  # to print the best performing city

# Q8: Efficiency(very important for business)
# create a column
# efficiency = profit / sales
# find the efficient customer
df['Efficiency'] = df['Profit'] / df['Sales']  # to create a new column 'Efficiency' in the DataFrame by calculating the ratio of 'Profit' to 'Sales'
efficient_customers = df[df['Efficiency'] > 0.5]['Customer'].unique()  # to filter the customers who are efficient by selecting the rows where Efficiency is greater than 0.5 and then getting the unique customer names
print("\nEfficient Customers:")
print(efficient_customers)  # to print the efficient customers

# “Find MOST efficient customer”
# ✅ Correct Answer
# most_efficient_customer = df.loc[df['Efficiency'].idxmax()]

# print(most_efficient_customer[['Customer', 'Efficiency']])


# Q9: top customer per city
# find the top customer with highest profit in each city
# top_customer_per_city = df.groupby('City').apply(lambda x: x.loc[x['Profit'].idxmax()])  # to find the top customer with the highest profit in each city by grouping the DataFrame by 'City' and applying a lambda function that selects the row with the maximum 'Profit' for each group
# # print(top_customer_per_city.columns)
# top_customer_per_city = df.groupby('City').apply(
#     lambda x: x.loc[x['Profit'].idxmax()]
# ).reset_index(drop=True)
# print("\nTop Customer per City:")
# print(df.columns.tolist())
# print(top_customer_per_city[['City', 'Customer', 'Profit']])  # to print the city, customer, and profit for the top customer in each city

top_customer_per_city = df.loc[
    df.groupby('City')['Profit'].idxmax()
]
print("\nTop Customer per City:")
print(top_customer_per_city[['City', 'Customer', 'Profit']])