import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sales = {
    'Sales': [1000,1500,1200,1800,2000],
    'Profit': [200,300,250,400,500],
    'Discount': [10,15,12,18,20]
}

# df = pd.DataFrame(sales)

df = pd.read_csv(r'D:\Python programing\Pandas\Matplotlib\Diwali Sales Data.csv', encoding='latin1')

# Q1: shape
print("===== Shape =====")
total_number_of_rows_n_columns = df.shape
print(total_number_of_rows_n_columns)

# Q2: info()
print("===== info =====")
print(df.info())

# Q3: Describe
print("===== Describe =====")
print(df.describe())

# Q4: isnull().sum()
print("===== Sum of null values =====")
print(df.isnull().sum())

# Q5: duplicate().sum()
print("===== Sum of Duplicate value =====")
print(df.duplicated().sum())

# Q6: unique values
print("===== Find nunique values =====")
print(df.nunique)

# Q7: Find top 5 customer by sales
top_5_customer = (
    df.groupby('Cust_name')['Amount']
    .sum()
    .sort_values(ascending=False)
    .head(5)
)
print(top_5_customer)
top_5_customer = top_5_customer.reset_index()

plt.figure(figsize=(10, 8))

sns.barplot(
    data=top_5_customer,
    x='Cust_name',
    y='Amount'
)

plt.title('Top 5 Customer by sales')
plt.xlabel('Customer')
plt.ylabel('Total Sales')

plt.xticks(rotation = 45)

plt.tight_layout()
plt.show()

# Q8: top 5 states by sales
top_5_states = (
    df.groupby('State')['Amount']
    .sum()
    .sort_index(ascending=False)
    .head(5)
)

print("+++++ Top 5 states +++++")
print(top_5_states)

top_5_states = top_5_states.reset_index()

plt.figure(figsize=(10, 8))

sns.barplot(
    data=top_5_states,
    x='State',
    y='Amount'
)

plt.title("Top 5 states")
plt.xlabel('State')
plt.ylabel('Amount')

plt.xticks(rotation = 45)

plt.tight_layout()
plt.show()
 

# Q9 Find region with highest sales
highest_sales_by_region = (
    df.groupby('Zone')['Amount']
    .sum()
    .sort_index(ascending=False)
    .head(5)
) 

print(highest_sales_by_region)

highest_sales_by_region = highest_sales_by_region.reset_index()

plt.figure(figsize=(10, 8))

sns.lineplot(
    data=highest_sales_by_region,
    x='Zone',
    y='Amount'
)

plt.title('Highest sales by zone')
plt.xlabel('Zone')
plt.ylabel('Amount')

plt.xticks(rotation = 45)

plt.tight_layout()
plt.show()

# Q10: Bussiness insights

# 1. The many time order done by Vishakha which is 382782, and second coustomer is sudevi
# which is 287142.
# 
# 2. The highest ordered done from state is utterpradesh which 19374968.
# 
# 3. highest zone which central 41600873