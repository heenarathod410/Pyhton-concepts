import pandas as pd

employees = pd.DataFrame({
    'Name': [' alice ', 'BOB', 'charlie'],
    'Email': [
        'alice@gmail.com',
        'bob@yahoo.com',
        'charlie@gmail.com'
    ],
    'Department': ['it', 'HR', 'finance']
})

# Q1: Remove extra spaces from 'Name' column
employees['Name'] = employees['Name'].str.strip()
print("After removing extra spaces from 'Name':")
print(employees['Name'])

# Q2: Convert 'Name' column to title case
employees['Name'] = employees['Name'].str.title()
print("After converting 'Name' to title case:")
print(employees['Name'])

# Q3: Convert 'Department' column to uppercase
employees['Department'] = employees['Department'].str.upper()
print("After converting 'Department' to uppercase:")
print(employees['Department'])

# Q4: Find employees with Gmail accounts
gmail_employees = employees[employees['Email'].str.contains('gmail')]
print("Employees with Gmail accounts:")
print(gmail_employees[['Name', 'Email']])

# Q5: Replace 'gmail.com' with 'company.com' in 'Email' column
employees['Email'] = employees['Email'].str.replace('gmail.com', 'company.com')
print("After replacing 'gmail.com' with 'company.com' in 'Email':")
print(employees['Email'])

# Q6: Extract the username from 'Email' column
employees['Username'] = employees['Email'].str.split('@').str[0]
print("After extracting username from 'Email':")
print(employees['Username'])

# Q7: Count the number of characters in 'Name' column
employees['Name_Length'] = employees['Name'].str.len()
print("Number of characters in 'Name':")
print(employees['Name_Length'])

# Q8: Check if 'Department' contains 'IT'
employees['Is_IT'] = employees['Department'].str.contains('IT')
print("Check if 'Department' contains 'IT':")
print(employees['Is_IT'])

# Q9: Sort employees by 'Name'
sorted_employees = employees.sort_values(by='Name')
print("Employees sorted by 'Name':")
print(sorted_employees)

# Q10: Find the first 3 characters of 'Name' column
employees['Name_First3'] = employees['Name'].str[:3]
print("First 3 characters of 'Name':")
print(employees['Name_First3'])

# Q11: Find the last 3 characters of 'Email' column
employees['Email_Last3'] = employees['Email'].str[-3:]
print("Last 3 characters of 'Email':")
print(employees['Email_Last3'])

# Q12: Check if 'Name' starts with 'A'
employees['Name_StartsWith_A'] = employees['Name'].str.startswith('A')
print("Check if 'Name' starts with 'A':")
print(employees['Name_StartsWith_A'])

# Q13: Check if 'Email' ends with 'company.com'
employees['Email_EndsWith_Company'] = employees['Email'].str.endswith('company.com')
print("Check if 'Email' ends with 'company.com':")
print(employees['Email_EndsWith_Company'])


# Q14: Find the number of words in 'Name' column
employees['Name_Word_Count'] = employees['Name'].str.split().str.len()
print("Number of words in 'Name':")
print(employees['Name_Word_Count'])
