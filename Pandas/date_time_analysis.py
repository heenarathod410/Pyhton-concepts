import pandas as pd

sales = pd.DataFrame({
    'Customer': ['A', 'B', 'C', 'D'],
    'Sales': [1000, 1500, 1200, 1800],
    'Order_Date': [
        '2024-01-10',
        '2024-02-15',
        '2024-02-20',
        '2024-03-05'
    ]
})

# Q1: convert 'Order_Date' to datetime
sales['Order_Date'] = pd.to_datetime(sales['Order_Date'])
print("After converting 'Order_Date' to datetime:")
print(sales['Order_Date'])

# Q2: extract year, month, day
sales['Year'] = sales['Order_Date'].dt.year
sales['Month'] = sales['Order_Date'].dt.month
sales['Day'] = sales['Order_Date'].dt.day
print("After extracting year, month, and day:")
print(sales[['Year', 'Month', 'Day']])

# Q3: find total sales per month
monthly_sales = sales.groupby('Month')['Sales'].sum()
print("Total sales per month:")
print(monthly_sales)

# Q4: find month with highest sales
highest_sales_month = monthly_sales.idxmax()
print(f"Month with highest sales: {highest_sales_month}")

# Q5: find sales made in fabruary
february_sales = sales[sales['Month'] == 2]['Sales'].sum()
print(f"Total sales made in February: {february_sales}")    

# Q6: sort data by 'Order_Date'
sorted_sales = sales.sort_values(by='Order_Date')
print("Data sorted by 'Order_Date':")
print(sorted_sales)