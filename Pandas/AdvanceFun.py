import pandas as pd

# # Sample DataFrames
# data1 = pd.DataFrame({
#     'ID': [1, 2, 3, 4],
#     'Name': ['Alice', 'Bob', 'Charlie', 'David'],
#     # 'Age': [25, 30, 35, 40]
#     'Marks': [35, 90, 25, 80],
#     'gender': ['F', 'M', 'M', 'M'],
#     'short_city_name': ['Raj', 'Srt', 'Raj', 'Jmn'],
#     'category':['medium', 'high', 'low', 'high']
# })

# sales = pd.DataFrame({
#     'ID': [1, 2, 3, 5, 6, 1],
#     'Product': ['A', 'B', 'C', 'D', 'E', 'A'],
#     'Amount': [100, 200, 150, 300, 250, 100],
#     'base_price': [80, 150, 120, 250, 200, 80],
#     'sale_price': [120, 250, 130, 350, 400, 120],
#     'Customer': ['alice', 'bob', 'charlie', 'bob', 'eve', 'alice'],
#     'city': ['Rajkot', 'Surat', 'Jamnagar', 'Rajkot','Rajkot', 'Rajkot']
# })

# # apply a function to create a new column based on existing columns
# data1['Result'] = data1['Marks'].apply(lambda x: 'Pass' if x >= 40 else 'Fail')
# print("DataFrame with Result Column:")
# print(data1)

# # Q1: profit status based on Amount
# sales['Profit'] = (sales['sale_price'] - sales['base_price'])
# sales['Profit_status'] = sales['Profit'].apply(lambda x: 'High Profit' if x > 100 else 'Low profit')
# print("\nSales DataFrame with Profit Status:")
# print(sales)

# # Q2: convert customer names to uppercase using apply()
# sales['Customer'] = sales['Customer'].apply(lambda x: x.upper())
# print("\nSales DataFrame with Uppercase Customer Names:")
# print(sales)

# # replace value usin map()
# data1['gender'] = data1['gender'].map({'M': 'Male', 'F': 'Female'})
# print("\nDataFrame with Gender Mapped to Full Form:")
# print(data1)

# # Q3: convert short city names to full names using map() 
# data1['City'] = data1['short_city_name'].map({'Raj': 'Rajkot', 'Srt': 'Surat', 'Jmn': 'Jamnagar'})
# print("\nDataFrame with Full City Names:")
# print(data1)

# # Q4: convert category to numeric values using map()
# data1['Category_Code'] = data1['category'].map({'low': 1, 'medium': 2, 'high': 3})
# print("\nDataFrame with Category Mapped to Numeric Codes:")
# print(data1)

# # Q5: use lambda to add 10% bonous to profit
# sales['Bonus'] = sales['Profit'].apply(lambda x: x * 0.1)
# print("\nSales DataFrame with Bonus Column:")
# print(sales)

# # Q6: create discount column using lambda function
# sales['Discount'] = sales['sale_price'].apply(lambda x: x * 0.2 if x > 150 else x * 0.1)
# print("\nSales DataFrame with Discount Column:")
# print(sales)

# # Q7: count customer per city using value_counts()
# customer_count_per_city = sales['city'].value_counts()
# print("\nCustomer Count per City:")
# print(customer_count_per_city)

# # Q8: number of high and low profit customers using value_counts()
# profit_status_counts = sales['Profit_status'].value_counts()
# print("\nProfit Status Counts:")
# print(profit_status_counts)

# # Q9: find unique city
# print("\nUnique City Names(show) in data1 DataFrame:")
# print(data1['short_city_name'].unique())

# print("\nUnique City Names(count) in data1 DataFrame:")
# print(data1['short_city_name'].nunique())

# # Q10: total unique customers in sales DataFrame
# total_unique_customers = sales['Customer'].nunique()
# print("\nTotal Unique Customers in Sales DataFrame:")
# print(total_unique_customers)

# # Example of transform()
# data1['avg_marks_city'] = data1.groupby('short_city_name')['Marks'].transform('mean')
# print("\nDataFrame with Transformed short_city_name:")
# print(data1)

# # Q1: calculate the average profit per city using transform()
# sales['avg_profit_city'] = sales.groupby('city')['Profit'].transform('mean')
# print("\nSales DataFrame with Average Profit per City:")
# print(sales)

# # Q2: create max sales per city using transform()
# sales['max_sales_city'] = sales.groupby('city')['sale_price'].transform('max')
# print("\nSales DataFrame with Max Sales per City:")
# print(sales)

# # Q3: customer whose sales above their city average using transform()
# sales['avg_sales_customer'] = sales.groupby('Customer')['sale_price'].transform('mean')
# sales['above_city_avg'] = sales['sale_price'] > sales['avg_sales_customer']
# print("\nSales DataFrame with Above City Average Sales:")
# print(sales)

# # Q4: minimum sales per city using transform()
# sales['min_sales_city'] = sales.groupby('city')['sale_price'].transform('min')
# print("\nSales DataFrame with Minimum Sales per City:")
# print(sales)

# # Q5: find customers whose profit is above the average profit of their city using transform()
# sales['above_city_avg'] = sales['Profit'] > sales.groupby('city')['Profit'].transform('mean')
# print("\nSales DataFrame with Customers Above City Average Profit:")
# print(sales)

# # Q6: rank of sales within each city using transform()
# sales['sales_rank_city'] = sales.groupby('city')['sale_price'].transform(lambda x: x.rank(ascending=False))
# print("\nSales DataFrame with Sales Rank within Each City:")
# print(sales)

# # find duplicate rows 
# # Q1: find duplicate rows using duplicated()
# duplicate_rows = sales[sales.duplicated()]
# print("\nDuplicate Rows in Sales DataFrame:")
# print(duplicate_rows)

# # Q2: remove duplicate rows using drop_duplicates()
# sales_no_duplicate = sales.drop_duplicates()
# print("\nSales DataFrame with Duplicate Rows Removed:")
# print(sales_no_duplicate)

# # Q3: find duplicate customers only using duplicated()
# # hint: subset parameter
# duplicate_rows =sales[sales.duplicated(subset=['Customer'])]
# print("\nDuplicate Customers in Sales DataFrame:")
# print(duplicate_rows)

# # Q4: keep latest duplicate and remove old ones using drop_duplicates()
# sales_no_duplicate = sales.drop_duplicates(subset=['Customer'], keep='last')
# print("\nSales DataFrame with Latest Duplicate Customers:")
# print(sales_no_duplicate)

# # Q5: count total duplicate rows using duplicated()
# total_duplicate_rows = sales.duplicated().sum()
# print("\nTotal Duplicate Rows in Sales DataFrame:")
# print(total_duplicate_rows)

students = pd.DataFrame({
    'ID': [1, 2, 3, 4],
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'math_score': [85, 90, 78, 92],
    'english_score': [88, 85, 90, 91],
    'science_score': [90, 92, 85, 88],
    'social_science_score': [80, 87, 89, 90],
    'hindi_score': [82, 88, 91, 89],
    'gender': ['F', 'M', 'M', 'M']
})

# Q1: convert math_score and science_score column into rows using melt()
melted_students = pd.melt(students,
                          id_vars = ['Name', 'ID', 'gender'],
                          value_vars=['math_score', 'science_score'],
                          var_name= 'Subject',
                          value_name='Score'
                          )
print("\nMelted Students DataFrame:")
print(melted_students)

# Q2: Keep Name fixed while melting
melted_students = pd.melt(students,
                          id_vars = ['Name'],
                          var_name= 'Subject',
                          value_name='Score'
                          )
print("\nMelted Students DataFrame with Name Fixed:")
print(melted_students)

# Q3: Rename: variable column -> subject and value column -> score
melted_students = pd.melt(students,
                          id_vars = ['Name'],
                          var_name= 'Subject',
                          value_name='Score'
                          )
print("\nMelted Students DataFrame with Renamed Columns:")
print(melted_students)

# Q4: find average marks per subject after melting
melted_students = pd.melt(students,
                          id_vars = ['Name'],
                          var_name= 'Subject',
                          value_name='Score',
                          value_vars=['math_score', 'english_score', 'science_score', 'social_science_score', 'hindi_score']
                          )
average_marks_per_subject = melted_students.groupby('Subject')['Score'].mean()
print("\nAverage Marks per Subject:")
print(average_marks_per_subject)

# Q5: find topper in each subject after
topper_per_subject = melted_students.loc[melted_students.groupby('Subject')['Score'].idxmax()]
print("\nTopper in Each Subject:")
print(topper_per_subject)

# Q6: Highest scoring students overall
students['total_score'] = students[['math_score', 'english_score', 'science_score', 'social_science_score', 'hindi_score']].sum(axis=1)
topper_overall = students.loc[students['total_score'].idxmax()]
print("\nHighest Scoring Student Overall:")
print(topper_overall)

# Q7: Average score by gender
average_score_by_gender = students.groupby('gender')['total_score'].mean()
print("\nAverage Score by Gender:")
print(average_score_by_gender)

# Q8: sort all students by score descending order
sorted_students = students.sort_values(by='total_score', ascending=False)
print("\nStudents Sorted by Total Score (Descending):")
print(sorted_students)

# explode()
orders = pd.DataFrame({
    'Customer': ['Alice', 'Bob', 'Charlie'],
    'Products': [
        ['Phone', 'Laptop'],
        ['Tablet'],
        ['Phone', 'Tablet', 'Watch']
    ]
})

# Q1: Explode product column using explode()
exploded_products = orders.explode('Products')
print("\nExploded Orders DataFrame:")   
print(exploded_products)

# Q2: count total products ordered using explode()
# hint: use value_counts() after explode
total_products_ordered = orders.explode('Products').value_counts()
print("\nTotal Products Ordered:")
print(total_products_ordered)

# Q3: find most ordered product using explode()
most_ordered_product = orders.explode('Products')['Products'].value_counts().idxmax()
print("\nMost Ordered Product:")
print(most_ordered_product)

# Q4: find customer who ordered phone
customers_who_ordered_phone = orders[orders['Products'].apply(lambda x: 'Phone' in x)]['Customer']
print("\nCustomers Who Ordered Phone:")
print(customers_who_ordered_phone)

# Q5: find products ordered by each customer using explode()
products_by_customer = orders.explode('Products').groupby('Customer')['Products'].apply(list)
print("\nProducts Ordered by Each Customer:")
print(products_by_customer)

# Q1: create overall rank using total_score
students['overall_rank'] = students['total_score'].rank(ascending=False)
print("\nStudents DataFrame with Overall Rank:")
print(students)

# Q2: create rank within gender
# hint use groupby() and rank()
students['gender_rank'] = students.groupby('gender')['total_score'].rank(ascending=False)
print("\nStudents DataFrame with Gender Rank:")
print(students)

# Q3: find top 2 students overall
top_2_students_overall = students.nsmallest(2, 'overall_rank')
print("\nTop 2 Students Overall:")
print(top_2_students_overall)

# Q4: find topper in each gender
topper_in_each_gender = students.loc[students.groupby('gender')['total_score'].idxmax()]
print("\nTopper in Each Gender:")
print(topper_in_each_gender)

# Q5: create dense rank
students['dense_rank'] = students['total_score'].rank(ascending=False, method='dense')
print("\nStudents DataFrame with Dense Rank:")
print(students)

# Q6: difference between rank and dense rank
students['rank_diff'] = students['overall_rank'] - students['dense_rank']
print("\nStudents DataFrame with Rank Difference:")
print(students)