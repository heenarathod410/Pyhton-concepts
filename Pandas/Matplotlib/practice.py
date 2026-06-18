import pandas as pd
import matplotlib.pyplot as plt
import os

sales = pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
    'Sales': [1000, 1500, 1200, 1800, 2000]
})


# Q1: Line chart of monthly sales
plt.plot(sales['Month'], sales['Sales'], marker='o')  # Line plot with markers

plt.title('Monthly Sales')
plt.xlabel('Month')
plt.ylabel('Sales')

# os.makedirs('charts', exist_ok=True)

plt.savefig('charts/monthly_sales.png')  # Save the figure as a PNG file
print(os.getcwd())
plt.show()

# Q2: Bar chart of monthly sales
plt.bar(sales['Month'], sales['Sales'])

plt.title('Monthly Sales')
plt.xlabel('Month')
plt.ylabel('Sales')

plt.savefig('charts/monthly_sales_bar.png')  # Save the figure as a PNG file
plt.show()

# Q3: Pie chart of sales distribution

plt.pie(
    sales['Sales'],
    labels=sales['Month'],
    autopct='%1.1f%%'
)

plt.title('Sales Distribution by Month')

plt.savefig('charts/sales_distribution_pie.png')  # Save the figure as a PNG file
plt.show()

# Q4: Histogram of sales values
plt.hist(sales['Sales'])

plt.title('Sales Distribution')

plt.savefig('charts/sales_distribution_histogram.png')  # Save the figure as a PNG file
plt.show()

# Figure
# Figure example: Adjusting figure size
plt.figure(figsize=(10, 6))  # Set figure size
plt.plot(sales['Month'], sales['Sales'], marker='o')
plt.title('Monthly Sales')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.savefig('charts/monthly_sales_large.png')  # Save the figure as a PNG file
plt.show()

# Grid
plt.plot(sales['Month'], sales['Sales'], marker='o')
plt.grid(True)  # Show grid
plt.title('Monthly Sales with Grid')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.savefig('charts/monthly_sales_grid.png')  # Save the figure as a PNG file
plt.show()

# Legend
plt.plot(sales['Month'], sales['Sales'], marker='o', label='Sales')
plt.title('Monthly Sales with Legend')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.legend()  # Show legend
plt.savefig('charts/monthly_sales_legend.png')  # Save the figure as a PNG file
plt.show()

# Scatter
students = pd.DataFrame({
    'Hours': [1,2,3,4,5],
    'Marks': [20,35,50,70,90]
})

plt.scatter(students['Hours'], students['Marks'])

plt.title('Hours vs Marks')
plt.xlabel('Hours Studied')
plt.ylabel('Marks Obtained')

plt.show()

# Brah

plt.barh(sales['Month'], sales['Sales'])
plt.title('Monthly Sales (Horizontal Bar)')
plt.xlabel('Sales')
plt.ylabel('Month')
plt.show()

# Q1:line chart with figsize(8,5), marker, and grid
plt.figure(figsize=(8, 5))
plt.plot(sales['Month'], sales['Sales'],marker='o')

plt.title('Monthly Sales')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.grid(True)

plt.savefig('charts/monthly_sales_figure.png')  # Save the figure as a PNG file
plt.show()

# Q2: line chart with label and legend
plt.plot(sales['Month'], sales['Sales'], marker='o', label='Sales')
plt.title('Monthly Sales with Legend')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.legend()

plt.savefig('charts/monthly_sales_legend.png')  # Save the figure as a PNG file
plt.show()

# Q3: create horizontal bar chart
plt.barh(sales['Month'], sales['Sales'])
plt.title('Monthly Sales (Horizontal Bar)')
plt.xlabel('Sales')
plt.ylabel('Month')
plt.savefig('charts/monthly_sales_horizontal.png')  # Save the figure as a PNG file
plt.show()


# Q4: create scatter plot 
plt.scatter(sales['Month'], sales['Sales'])
plt.title('Monthly Sales Scatter Plot')
plt.xlabel('Month')
plt.ylabel('Sales') 
plt.savefig('charts/monthly_sales_scatter.png')  # Save the figure as a PNG file
plt.show()

# Q5: save charts into 'charts' folder

# Q1: create line chart with color = 'green', linestyle = '--', and marker = 'o'
plt.figure(figsize=(8, 5))

plt.plot(sales['Month'],sales['Sales'], color='green', linestyle='--', marker='o')
plt.title('Monthly Sales with Custom Style')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.grid(True)
plt.savefig('charts/monthly_sales_custom.png')  # Save the figure as a PNG file
plt.show()

# Q2: create bar chart with color = 'orange'
plt.figure(figsize=(8, 5))
plt.bar(sales['Month'], sales['Sales'], color='orange')
plt.title('Monthly Sales (Orange Bar)')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.savefig('charts/monthly_sales_orange.png')  # Save the figure as a PNG
plt.show()

# Q3: Rotate month labels 
plt.figure(figsize=(8, 5))
plt.plot(sales['Month'], sales['Sales'], marker='o')
plt.title('Monthly Sales with Rotated Labels')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.xticks(rotation=45)  # Rotate x-axis labels by 45 degrees
plt.grid(True)
plt.tight_layout()
plt.savefig('charts/monthly_sales_rotated.png')  # Save the figure as a PNG file
plt.show()

# Q4: create two charts in one figure using subplots
# top = line chart, bottom = bar chart
plt.figure(figsize=(10, 8))

plt.subplot(2, 1, 1)  # First subplot (line chart)
plt.plot(sales['Month'], sales['Sales'], marker='o', color='blue')
plt.title('Monthly Sales (Line Chart)')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.grid(True)

plt.subplot(2, 1, 2)  # Second subplot (bar chart)
plt.bar(sales['Month'], sales['Sales'], color='orange')
plt.title('Monthly Sales (Bar Chart)')
plt.xlabel('Month')
plt.ylabel('Sales')


plt.tight_layout()
plt.savefig('charts/monthly_sales_subplots.png')  # Save the figure as a PNG file
plt.show()

# Annotations
# Q1: create bar chart
# Q2: show sales value above bars
# Q3: charts/bar_chart_with_values.png

plt.figure(figsize=(8, 5))
plt.bar(sales['Month'], sales['Sales'], color='skyblue')
plt.title('Monthly Sales with Values')
plt.xlabel('Month')
plt.ylabel('Sales')
# Show sales value above bars
for index, value in enumerate(sales['Sales']):
    plt.text(index, value + 50, str(value), ha='center')  # Adjust position as needed
plt.tight_layout()
plt.savefig('charts/bar_chart_with_values.png')  # Save the figure as a PNG file
plt.show()

sales['Profit'] = [200, 300, 250, 400, 500]
print(sales)

# Multiple Lines in One Chart
# Q1: create on chart with sales line and profit line
# Q2: use different markers sales = 'o' and profit = 's'
# Q3: Add legend, grid and title
# Q4: charts/sales_vs_profit.png

plt.figure(figsize=(8, 5))
plt.plot(sales['Month'], sales['Sales'], marker='o', label='Sales')
plt.plot(sales['Month'], sales['Profit'], marker='s', label='Profit')
plt.title('Sales vs Profit')
plt.xlabel('Month')
plt.ylabel('Amount')
plt.legend()
plt.grid(True)
plt.savefig('charts/sales_vs_profit.png')  # Save the figure as a PNG file
plt.show()


# Final Matplotlib Challenge

sales = pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
    'Sales': [1000, 1500, 1200, 1800, 2000],
    'Profit': [200, 300, 250, 400, 500]
})

#Q1: create a chart with
# sales line,
# profit line,
# different markers for sales and profit,
# legend, grid, title, and save it as 'charts/sales_profit_comparison.png'

# Q2: add values above sales and profit lines

# Q3: rotate month labels by 45 degrees

plt.figure(figsize=(10, 6))
plt.plot(sales['Month'], sales['Sales'], marker='o', label='Sales')
plt.plot(sales['Month'], sales['Profit'], marker='s', label='Profit')
plt.title('Sales vs Profit Comparison')
plt.xlabel('Month')
plt.ylabel('Amount')
plt.legend()
plt.grid(True)
# Add values above sales and profit lines
for index, value in enumerate(sales['Sales']):
    plt.text(index, value + 50, str(value), ha='center')  # Sales values
for index, value in enumerate(sales['Profit']):
    plt.text(index, value * 1.02, str(value), ha='center')  # Profit values

plt.xticks(rotation=45)  # Rotate month labels by 45 degrees

plt.tight_layout()
plt.savefig('charts/final_dashboard_chart.png')  # Save the figure as a PNG file
plt.show()

