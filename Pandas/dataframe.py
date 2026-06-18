import pandas as pd

# create a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Marks': [80, 60, 90],
    'City': ['Rajkot', 'Jamnagar', 'Surat']
}

df = pd.DataFrame(data)
print(df)

# Accessing data
# 🧠 “Give me marks column”
print("Marks column:")
print(df['Marks'])  # to print the Marks column

# 🧠 “Give me name + marks”
print("\nName and Marks columns:")
print(df[['Name', 'Marks']])  # to print the Name and Marks columns

# 🧠 “Give me the first row”
print("\nFirst row:")
print(df.iloc[0])  # to print the first row of the DataFrame

# Adding a new column
df['Grade'] = df['Marks'].apply(lambda x: 'A' if x >= 90 else ('B' if x >= 60 else 'C'))  # to add a new column 'Grade' based on the Marks
print("\nDataFrame with Grade column:")
print(df)

# better way to add grade column
df['Grade'] = (df['Marks']>40).map({True: 'Pass', False: 'Fail'})  # to add a new column 'Grade' based on whether the Marks are greater than 40
print("\nDataFrame with Pass/Fail Grade column:")
print(df)

# sorting the DataFrame
print("\nDataFrame sorted by Marks:")
print(df.sort_values(by='Marks', ascending=False))  # to print the DataFrame sorted by Marks in descending order


# grouping the DataFrame
print("\nAverage Marks by Grade:")
print(df.groupby('Grade')['Marks'].mean())  # to print the average Marks for each Grade group

# grouping by City
print("\nAverage Marks by City:")
print(df.groupby('City')['Marks'].mean())  # to print the average Marks for each City group

# merging two DataFrames
data2 = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [20, 21, 22]
}
df2 = pd.DataFrame(data2)
merged_df = pd.merge(df, df2, on='Name')  # to merge the two DataFrames on the 'Name' column
print("\nMerged DataFrame:")
print(merged_df)  # to print the merged DataFrame

# 👉 Your Tasks
# Q1: Show students from Rajkot
# Q2: Show students who scored > 50
# Q3: Add Result column (Pass/Fail)
# Q4: Find average marks per city

# Q1: Show students from Rajkot
rajkot_students = df[df['City'] == 'Rajkot']  # to filter the students from Rajkot
print("\nStudents from Rajkot:")
print(rajkot_students)  # to print the students from Rajkot

# 🔥 Upgrade 1: Select Only Needed Columns
rajkot_students_names = df[df['City'] == 'Rajkot']['Name']  # to filter the students from Rajkot and select only their names
print("\nNames of students from Rajkot:")
print(rajkot_students_names)  # to print the names of students from Rajkot

# Q2: Show students who scored > 50
students_above_50 = df[df['Marks'] > 50]  # to filter the students who scored greater than 50
print("\nStudents who scored > 50:")
print(students_above_50)  # to print the students who scored greater than 50

# Q3: Add Result column (Pass/Fail)
df['Result'] = (df['Marks'] > 40).map({True: 'Pass', False: 'Fail'})  # to add a new column 'Result' based on whether the Marks are greater than 40
print("\nDataFrame with Result column:")
print(df)  # to print the DataFrame with the new Result column

# 🔥 Upgrade 2: Select Only Needed Columns
df['Result'] = ['Pass' if x > 40 else 'Fail' for x in df['Marks']]  # to add a new column 'Result' based on whether the Marks are greater than 40 using list comprehension
print("\nDataFrame with Result column using list comprehension:")
print(df)  # to print the DataFrame with the new Result column added using list comprehension


# Q4: Find average marks per city
average_marks_per_city = df.groupby('City')['Marks'].mean()  # to calculate the average marks for each city
print("\nAverage marks per city:")
print(average_marks_per_city)  # to print the average marks for each city

# 🎯 Q5: Topper from Each City
# Rajkot → highest marks student
# Surat → highest marks student

# 🎯 Q6: Students who failed AND from Rajkot

# City = Rajkot
# Marks ≤ 40

# 🎯 Q7: Add Grade Column

# Rule:

# ≥ 80 → A
# ≥ 50 → B
# < 50 → C

# 🎯 Q8 (Important):
# 👉 Find city with highest average marks

# Q5: Topper from Each City
topper_per_city = df.loc[df.groupby('City')['Marks'].idxmax()]  # to find the student with the highest marks in each city
print("\nTopper from each city:")  
print(topper_per_city)  # to print the toppers from each city

# 🔥 Upgrade (Cleaner Output)
topper_per_city = df.loc[df.groupby('City')['Marks'].idxmax()][['City', 'Name', 'Marks']]
print("\nTopper from each city (cleaner output):")
print(topper_per_city)  # to print the toppers from each city with only City, Name, and Marks columns

# Q6: Students who failed AND from Rajkot
failed_rajkot_students = df[(df['City'] == 'Rajkot') & (df['Marks'] <= 40)]  # to filter the students who failed and are from Rajkot
print("\nStudents who failed and are from Rajkot:")
print(failed_rajkot_students)  # to print the students who failed and are from Rajkot

# Q7: Add Grade Column
def assign_grade(marks):
    if marks >= 80:
        return 'A'
    elif marks >= 50:
        return 'B'
    else:
        return 'C'
df['Grade'] = df['Marks'].apply(assign_grade)  # to apply the assign_grade function to the Marks column and create a new Grade column
print("\nDataFrame with Grade column:")
print(df)  # to print the DataFrame with the new Grade column

# 🔥 Upgrade (Pro Way – No apply)
df['Grade'] = pd.cut(
    df['Marks'],
    bins=[0, 49, 79, 100],
    labels=['C', 'B', 'A']
)  # to create a Grade column based on the Marks using pd.cut for better performance
print("\nDataFrame with Grade column using pd.cut:")
print(df)  # to print the DataFrame with the new Grade column created using pd.cut


# Q8: Find city with highest average marks
average_marks_per_city = df.groupby('City')['Marks'].mean()  # to calculate the average marks for each city
city_with_highest_average = average_marks_per_city.idxmax()  # to find the city with the highest average marks
print("\nCity with the highest average marks:")
print(city_with_highest_average)  # to print the city with the highest average marks

# Q-9 multi-conddition analysis
# 👉 Find students are from rajkot or surat and scored > 50 
rajkot_or_surat_students_above_50 = df[((df['City'] == 'Rajkot') | (df['City'] == 'Surat')) & (df['Marks'] > 50)]  # to filter the students who are from Rajkot or Surat and scored greater than 50
print("\nStudents from Rajkot or Surat who scored > 50:")
print(rajkot_or_surat_students_above_50)  # to print the students who are from Rajkot or Surat and scored greater than 50

# cleaner version
df['City'].isin(['Rajkot', 'Surat']) & (df['Marks'] > 50)  # to create a boolean mask for students from Rajkot or Surat and scored greater than 50
print("\nStudents from Rajkot or Surat who scored > 50 (cleaner version):")
print(df[df['City'].isin(['Rajkot', 'Surat']) & (df['Marks'] > 50)])  # to print the students who are from Rajkot or Surat and scored greater than 50 using the cleaner version

# Q - 10: Data insight
# marks >= 75 → Excellent
# marks >= 50 → Good
# marks < 50 → Needs Improvement
df['Performance'] = pd.cut(
    df['Marks'],
    bins=[-1, 49, 74, 100],
    labels=['Needs Improvement', 'Good', 'Excellent']
)  # to create a Performance column based on the Marks using pd.cut
print("\nDataFrame with Performance column:")
print(df)  # to print the DataFrame with the new Performance column

# Q-11: (Advanced)
# top 2 students overall
# and show only 2 columns (Name and Marks)
top_2_students = df.nlargest(2, 'Marks')[['Name', 'Marks']]  # to find the top 2 students based on Marks and select only the Name and Marks columns
print("\nTop 2 students overall:")
print(top_2_students)  # to print the top 2 students overall with only Name and Marks columns

# bonus thinking
# if interviewer asks: "what if tie?"
df.sort_values(by='Marks', ascending=False).head(2)  # to sort the DataFrame by Marks in descending order and get the top 2 rows, which will include ties if they exist
print("\nTop 2 students overall (including ties):")
print(df.sort_values(by='Marks', ascending=False).head(2))  # to print the top 2 students overall including ties if they exist