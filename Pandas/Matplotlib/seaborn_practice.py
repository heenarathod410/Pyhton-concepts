import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# Sample data
sales = pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
    'Sales': [1000, 1500, 1200, 1800, 2000]
})

sns.barplot(
    data=sales,
    x='Month',
    y='Sales'
)

# plt.show()

sales = pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
    'Sales': [1000, 1500, 1200, 1800, 2000],
    'Profit': [200, 300, 250, 400, 500]
})

# Q1: seaborn bar plot for sales by month
sns.barplot(
    data=sales,
    x='Month',
    y='Sales'
)
# plt.show()

# Q2: seaborn line plot for sales trend
sns.lineplot(
    data=sales,
    x='Month',
    y='Sales'
)
# plt.show()

# Q3: seaborn scatter plot for sales vs profit
sns.scatterplot(
    data=sales,
    x='Sales',
    y='Profit'
)
# plt.show()

# Q4: seaborn histogram for sales distribution
sns.histplot(
    data=sales,
    x='Sales',
    bins=5
)
# plt.show()

# Q5: seaborn box plot for sales
sns.boxplot(
    data=sales,
    y='Sales'
)
# plt.show()

# Q6: create a employee dataframe and use countplot

employees = pd.DataFrame({
    'Department': ['HR', 'IT', 'Finance', 'IT', 'HR', 'Finance', 'IT', 'HR'],
    'Employee': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Heidi']
})
sns.countplot(
    data=employees,
    x='Department'
)
# plt.show()

sales = pd.DataFrame({
    'Month': ['Jan','Jan','Feb','Feb'],
    'Sales': [1000,1200,1500,1400],
    'Region': ['East','West','East','West']
})

sns.barplot(
    data=sales,
    x='Month',
    y='Sales',
    hue='Region'
)
# plt.show()

sales = pd.DataFrame({
    'Month': ['Jan','Jan','Feb','Feb','Mar','Mar'],
    'Sales': [1000,1200,1500,1400,1700,1600],
    'Profit': [200,250,300,280,350,330],
    'Region': ['East','West','East','West','East','West']
})

# Q1: boxplot month vs sales with hue region
sns.boxplot(
    data=sales,
    x='Month',
    y='Sales',
    hue='Region'
)
# plt.show()

# Q2: lineplot month vs profit with hue region
sns.lineplot(
    data=sales,
    x='Month',
    y='Profit',
    hue='Region'
)
# plt.show()

sales = pd.DataFrame({
    'Month': ['Jan','Jan','Feb','Feb'],
    'Sales': [1000,1200,1500,1400],
    'Region': ['East','West','East','West']
})

sns.barplot(
    data=sales,
    x='Month',
    y='Sales',
    hue='Region'
)
# plt.show()

sales = pd.DataFrame({
    'Month': ['Jan','Jan','Feb','Feb','Mar','Mar'],
    'Sales': [1000,1200,1500,1400,1700,1600],
    'Profit': [200,250,300,280,350,330],
    'Region': ['East','West','East','West','East','West']
})

# Q1: barplot Months vs Sales

plt.figure(figsize=(10,8))

sns.barplot(
    data=sales,
    x='Month',
    y='Sales',
    hue='Region'
)

plt.title("Months Vs Sales")
plt.grid(True)

plt.tight_layout()

plt.savefig('charts/seabotn_months_vs_sales.png')
# plt.show()

# Q2: Lineplot months vs profit

plt.figure(figsize=(10,8))

sns.lineplot(
    data=sales,
    x='Month',
    y='Profit',
    hue='Region'
)

plt.title('Months vs Profit')
plt.grid(True)

plt.tight_layout()
plt.savefig('charts/seaborn_month_profit.png')

# plt.show()

# Q3: Scatter plt
sns.scatterplot(
    data=sales,
    x='Sales',
    y='Profit',
    hue='Region'
)
plt.title('Sales vs Profit')
plt.grid(True)

plt.tight_layout()
plt.savefig('charts/seaborn_sales_profit.png')

# plt.show()


# Correlation Heatmap
corr = sales[['Sales','Profit']].corr()

sns.heatmap(
    corr,
    annot=True
)

# plt.show()

sales = pd.DataFrame({
    'Sales': [1000,1500,1200,1800,2000],
    'Profit': [200,300,250,400,500],
    'Discount': [10,15,12,18,20]
})

#Q1: create correlation matrix
corr = sales[['Sales','Profit']].corr()

# Q2: create heatmap
sns.heatmap(
    corr,
    annot=True
)

plt.title('Correlation between sales and profit')

plt.tight_layout()
plt.savefig('charts/correlation_heatmap.png')

# plt.show()

# Pairplot
sales = pd.DataFrame({
    'Sales': [1000,1500,1200,1800,2000],
    'Profit': [200,300,250,400,500],
    'Discount': [10,15,12,18,20]
})

sns.pairplot(sales)
plt.show()

sales_data = pd.DataFrame({
    'Sales': [1000, 1500, 1200, 1800, 2000],
    'Profit': [200, 300, 250, 400, 500],
    'Discount': [10, 15, 12, 18, 20],
    'Quantity': [5, 8, 6, 10, 12]
})

# Q1: Create 
plt.figure(figsize=(10,8))
sns.pairplot(sales_data)

# Q2: Add title
plt.suptitle(
    'Sales dataset pairplot',
    y=1.02
    )

plt.tight_layout()
plt.show()