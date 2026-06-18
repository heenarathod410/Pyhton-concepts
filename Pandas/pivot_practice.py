import pandas as pd

# Sample data
data = {
    'City': ['New York', 'Los Angeles', 'New York', 'Chicago', 'Los Angeles'],
    'Customer': ['A', 'B', 'A', 'C', 'B'],
    'Profit': [100, 200, 150, 300, 250]
}
df = pd.DataFrame(data)

# create pivot table
pivot_table = df.pivot_table(values='Profit', index='City', columns='Customer', aggfunc='sum')
print(pivot_table)

# pivot table using csv file
df_csv = pd.read_csv(r'D:\Python programing\sales\100 Sales Records.csv')
pivot_table_csv = df_csv.pivot_table(values='Total Profit', index='Country', columns='Region', aggfunc='sum')
print(pivot_table_csv.to_string())
# save pivot table to csv
# pivot_table_csv.to_csv(r'D:\Python programing\sales\pivot_table.csv')

# Q1: total sale by region
sales = pd.read_csv(r'D:\Python programing\sales\100 Sales Records.csv')
total_sale_by_region = sales.pivot_table(values='Total Profit', index='Country', aggfunc='sum')
print("\nTotal Sales by Region:")
print(total_sale_by_region)
# total_sale_by_region.to_csv(r'D:\Python programing\sales\total_sale_by_region.csv')

# Q2: average profit by country
average_profit_by_country = sales.pivot_table(values='Total Profit', index='Country', aggfunc='mean')
print("\nAverage Profit by Country:")
print(average_profit_by_country)
# average_profit_by_country.to_csv(r'D:\Python programing\sales\average_profit_by_country.csv')

# Q3: total sale per item type
total_sale_per_item_type = sales.pivot_table(values='Total Profit', index='Item Type', aggfunc='sum')
print("\nTotal Sales per Item Type:")
print(total_sale_per_item_type)
# total_sale_per_item_type.to_csv(r'D:\Python programing\sales\total_sale_per_item_type.csv')

# Q4: country wise item type sales channel total profit
country_item_sales_channel_profit = sales.pivot_table(values='Total Profit', index=['Country', 'Item Type'], columns='Sales Channel', aggfunc='sum')
print("\nCountry-wise Item Type Sales Channel Total Profit:")
print(country_item_sales_channel_profit)
# country_item_sales_channel_profit.to_csv(r'D:\Python programing\sales\country_item_sales_channel_profit.csv') 