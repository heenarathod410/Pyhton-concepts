import pandas as pd

employees = pd.DataFrame({
    'Emp_ID': [1, 2, 3, 4],
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Department': ['IT', 'HR', 'Finance', 'IT']
})

salary = pd.DataFrame({
    'Emp_ID': [1, 2, 4, 5],
    'Salary': [50000, 60000, 70000, 80000]
})

# 🧠 LEVEL 1: Basic Merge
# Q1: Perform inner join
# show only matching employees with their salary
inner_join = pd.merge(employees, salary, on='Emp_ID', how='inner')
print("Inner Join:")
print(inner_join)

# Q2: Perform left join
# keep all employees even if salary is missing
left_join = pd.merge(employees, salary, on='Emp_ID', how='left')
print("\nLeft Join:")
print(left_join)

# Q3: Perform outer join
# keep everything from both tables
outer_join = pd.merge(employees, salary, on='Emp_ID', how='outer')
print("\nOuter Join:")
print(outer_join)

# Level 2
# Q4: find employee with missing salary
# isnull() will return True for rows where Salary is missing
missing_salary = left_join[left_join['Salary'].isnull()]
print("\nEmployees with Missing Salary:")
print(missing_salary)

# Q5: Find hieghest paid employee
highest_paid = inner_join[inner_join['Salary'] == inner_join['Salary'].max()]
print("\nHighest Paid Employee:")
print(highest_paid)

# Q6: Average salary per department
avg_salary = inner_join.groupby('Department')['Salary'].mean().reset_index()
print("\nAverage Salary per Department:")
print(avg_salary)

# Q7: Add salary category
def salary_category(salary):
    if salary >= 70000:
        return 'High'
    elif salary >= 50000:
        return 'Medium'
    else:
        return 'Low'
inner_join['Salary_Category'] = inner_join['Salary'].apply(salary_category)
print("\nEmployees with Salary Category:")
print(inner_join)

# Q8: which department has the highest average salary
highest_avg_salary_dept = avg_salary[avg_salary['Salary'] == avg_salary['Salary'].max()]
print("\nDepartment with Highest Average Salary:")
print(highest_avg_salary_dept)

# Q9: Advance
projects = pd.DataFrame({
    'Emp_ID': [1, 2, 3],
    'Project': ['AI', 'HRMS', 'Finance App']
})

# merge all three tables to get employee details, salary and project
employee_details = pd.merge(employees, salary, on='Emp_ID', how='left')
employee_details = pd.merge(employee_details, projects, on='Emp_ID', how='left')
print("\nEmployee Details with Salary and Project:")
print(employee_details)
