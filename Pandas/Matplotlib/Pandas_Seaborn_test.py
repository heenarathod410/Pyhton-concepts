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
print(df.nunique())

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
    # .sort_index(ascending=False)
    .sort_values(ascending=False)
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
    # .sort_index(ascending=False)
    .sort_values(ascending=False)
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

# Business Insights

# 1. Vishakha is the highest-value customer with total sales of 382,782, followed by Sudevi with sales of 287,142. These customers contribute significantly to revenue and should be targeted with loyalty and retention programs.

# 2. Uttar Pradesh generated the highest sales amount of 19,374,968, indicating a strong market presence. Marketing and inventory investments in this state may yield higher returns.

# 3. The Central zone recorded the highest sales of 41,600,873, making it the best-performing region. Understanding the factors driving this performance can help replicate success in other zones.


# Sales by gender
sales_by_gender = (df.groupby('Gender')['Amount'].sum())

print(sales_by_gender)

sales_by_gender = sales_by_gender.reset_index()

plt.figure(figsize=(10,8))

sns.barplot(
    data=sales_by_gender,
    x='Gender',
    y='Amount'
)

plt.title("Sales by gender")
plt.xlabel('Gender')
plt.ylabel('Amount')

plt.xticks(rotation = 45)

plt.tight_layout()
plt.show()

# Sales by Age Group
sales_by_age = (df.groupby('Age Group')['Amount']).sum()
print(sales_by_age)

sales_by_age = sales_by_age.reset_index()

plt.figure(figsize=(10,8))

sns.barplot(
    data=sales_by_age,
    x='Age Group',
    y='Amount'
)

plt.title("Sales by age")
plt.xlabel('Age')
plt.ylabel('Amount')

plt.xticks(rotation = 45)

plt.tight_layout()
plt.show()

# # Sales by Occupation

sales_by_occupation = df.groupby('Occupation')['Amount'].sum()
print(sales_by_occupation)

sales_by_occupation = sales_by_occupation.reset_index()

plt.figure(figsize=(10,8))

sns.barplot(
    data=sales_by_occupation,
    x='Occupation',
    y='Amount'
)

plt.title("Sales by occupation")
plt.xlabel('Occupation')
plt.ylabel('Amount')

plt.xticks(rotation = 45)

plt.tight_layout()
plt.show()

# Top 5 Product Categories
top_5_product = (df.groupby('Product_Category')['Amount']
                 .sum()
                #  .sort_index(ascending=False)
                # This sorts alphabetically.
                .sort_values(ascending=False)
                # This gives the actual top-selling categories.
                 .head(5))
print(top_5_product)

top_5_product = top_5_product.reset_index()

plt.figure(figsize=(10,8))

sns.barplot(
    data=top_5_product,
    x='Product_Category',
    y='Amount'
)

plt.title("Top 5 Product category")
plt.xlabel('Product_Category')
plt.ylabel('Amount')

plt.xticks(rotation = 45)

plt.tight_layout()
plt.show()

# Average Order Value
total_sales = df['Amount'].sum()
total_orders = df['Orders'].sum() 

Average_Order_Value = total_sales/total_orders

print("Average Order Value:", round(Average_Order_Value, 2))


# # Most Popular Product Category
popular_category = (
    df.groupby('Product_Category')['Amount']
      .sum()
      .idxmax()
)

print("Most Popular Category:", popular_category)

# Q11: Top 10 Products
top_10_products = (df.groupby('Product_ID')['Amount']\
                    .sum()\
                    .sort_values()\
                    .head(10)
)
print("Top 10 products", top_10_products)

top_10_products = top_10_products.reset_index()

plt.figure(figsize=(10,8))

sns.barplot(
    data=top_10_products,
    x='Product_ID',
    y='Amount'
)

plt.title("Top 10 Products")
plt.xlabel('Product_ID')
plt.ylabel('Amount')

plt.xticks(rotation = 45)

plt.tight_layout()
plt.show()

# Q12: Sales Distribution
plt.figure(figsize=(10,8))

sns.histplot(
    data=df,
    x='Amount',
    bins=20
)

plt.title("Sales Distribution")
plt.xlabel('Amount')

plt.tight_layout()
plt.show()

print(df['Amount'].describe())

# Question:

# Are most orders small or large?

# Sales amounts are concentrated in the ₹4,000–₹12,000 range, indicating that most 
# customer purchases are small to medium-sized. High-value orders above ₹15,000 occur 
# less frequently but contribute significantly to overall revenue. The business may 
# increase revenue by encouraging medium-value customers to make larger purchases through 
# bundle offers, cross-selling, and premium product recommendations.


# Q13: Correlation
corr = df[['Amount','Orders']].corr()

plt.figure(figsize=(10,8))

sns.heatmap(
    corr,
    annot=True
)

plt.title("Correlation")

plt.tight_layout()
plt.show()

# Question:

# Do customers who place more orders generate more sales?

# There is virtually no correlation (-0.013) between the number of orders and the sales 
# amount. This suggests that customers placing more orders do not necessarily generate 
# higher sales revenue. Some customers may place many small orders, while others may 
# generate high revenue through a few large purchases.

# The correlation between Orders and Amount is -0.013, indicating almost no 
# relationship between order count and sales value. Revenue growth may depend more on 
# increasing the value of individual transactions rather than simply increasing the 
# number of orders.

