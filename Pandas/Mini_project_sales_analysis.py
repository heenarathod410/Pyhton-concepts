import pandas as pd

# Dataset (we’ll simulate)
data = {
    'Customer': ['A', 'B', 'C', 'D', 'E'],
    'City': ['Rajkot', 'Surat', 'Rajkot', 'Jamnagar', 'Surat'],
    'Sales': [1000, 2000, 1500, 800, 2500],
    'Cost': [700, 1200, 1000, 500, 1500]
}
df = pd.DataFrame(data)

# Q1: create a profit column
df['Profit'] = df['Sales'] - df['Cost']
print("DataFrame with Profit column:")
print(df)

# Q2: find total profit
total_profit = df['Profit'].sum()
print("\nTotal Profit:", total_profit)

# Q3: profit per city
profit_per_city = df.groupby('City')['Profit'].sum()
print("\nProfit per City:")
print(profit_per_city)

# Q4: most profitable customer
most_profitable_customer = df.loc[df['Profit'].idxmax(), 'Customer']
print("\nMost Profitable Customer:", most_profitable_customer)

# Q5: customer with profit > 500
profitable_customers = df[df['Profit'] > 500]['Customer']
print("\nCustomers with Profit > 500:")
print(profitable_customers)

# PROFIT category
# create column 
# profit >= 1000 -> High
# profit >= 500 and < 1000 -> Medium
# profit < 500 -> Low
def profit_category(profit):
    if profit >= 1000:
        return 'High'
    elif profit >= 500:
        return 'Medium'
    else:
        return 'Low'
df['Profit Category'] = df['Profit'].apply(profit_category)
print("\nDataFrame with Profit Category:")
print(df)

# Q:7 Best performing city
# city with highest total profit
best_performing_city = df.groupby('City')['Profit'].sum().idxmax()
print("\nBest Performing City:", best_performing_city)

# Q8: loass detection
# find customers where profit is negative
loss_customers = df[df['Profit'] < 0]['Customer']
print("\nCustomers with Loss:")
print(loss_customers)

# Q9: (Advance)
# top customers in each city based on profit
# hint similar to idxmax() + groupby
top_customers_per_city = df.groupby('City').apply(lambda x: x.loc[x['Profit'].idxmax(), 'Customer'])
print("\nTop Customers per City:")
print(top_customers_per_city)