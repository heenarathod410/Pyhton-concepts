import pandas as pd

# create a Series
s = pd.Series([1, 2, 3, 4, 5])
print(s)  # to print the Series

# Return the value using the index
print(s[0])  # to print the value at index 0

# create a Series with custom index
s = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
print(s)  # to print the Series with custom index

# Access data by label
print(s['a'])  # to print the value at index 'a'

# Access data by position
print(s.iloc[0])  # to print the value at position 0

# modify the data 
s['a'] = 10
print(s)  # to print the modified Series

# Filtering data
print(s[s > 2])  # to print the values greater than 2

# Operations on Series
s1 = pd.Series([1, 2, 3])
s1 + 5  # to add 5 to each element in the Series
print(s1 + 5)  # to print the result of adding 5 to each element in the Series

# functions on Series
print(s1.mean())  # to print the mean of the Series
print(s1.sum())  # to print the sum of the Series
print(s1.min())  # to print the minimum value in the Series
print(s1.max())  # to print the maximum value in the Series

# Apply
print(s1.apply(lambda x: x * 2))  # to apply a function that multiplies each element by 2

marks = pd.Series([35, 80, 60, 20, 95], index=['Alice', 'Bob', 'Charlie', 'David', 'Eve'])
# 👉 Now think like teacher:

# Show marks of student B
# Add 10 marks to all
# Show only students who passed (>40)
# Create result (Pass/Fail)

# Show marks of student B
print(marks['Bob'])  # to print the marks of student Bob

# Add 10 marks to all
print(marks + 10)  # to print the marks of all students after adding 10

# Show only students who passed (>40)
print(marks[marks > 40])  # to print the marks of students who passed

# Create result (Pass/Fail)
result = marks.apply(lambda x: 'Pass' if x > 40 else 'Fail')  # to create a Series with Pass/Fail based on the marks
print(result)  # to print the result of pass/fail evaluation

# practice
# Q-1 Find average marks
# what is class average?
average_marks = marks.mean()  # to calculate the average marks of the class
print("Average marks of the class:")  # to print a message before the average marks
print(average_marks)  # to print the average marks of the class

#Q-2Who scored above average?
above_average = marks[marks > average_marks]  # to filter the marks of students who scored above average
print("Students who scored above average:")  # to print a message before the list of students
print(above_average)  # to print the marks of students who scored above average

# Q-3 count how many students passed
# how many students passed?
passed_students = marks[marks > 40]
print("Number of students who passed:")  # to print a message before the count
print(len(passed_students))  # to print the count of students who passed

# Q-4 who scored the highest marks?
highest_marks = marks.max()  # to find the highest marks scored by any student
print("Highest marks scored:")  # to print a message before the highest marks
print(highest_marks)  # to print the highest marks scored
topper = marks.idxmax() 
print("Topper:", topper)  # to print the name of the student who scored the highest marks

# Q-5 Grade system
def grade(marks):
    if marks >= 90:
        return 'A'
    elif marks >= 80:
        return 'B'
    elif marks >= 70:
        return 'C'
    elif marks >= 60:
        return 'D'
    else:
        return 'F'
grades = marks.apply(grade)  # to apply the grade function to each student's marks
print("Grades of students:")  # to print a message before the grades
print(grades)  # to print the grades of all students

# Q-6 Bonus marks
# Add 5 bonus marks to only who failed
bonus_marks = marks.apply(lambda x: x + 5 if x <= 40 else x)  # to add 5 bonus marks to students who failed
print("Marks after adding bonus:")  # to print a message before the marks after adding bonus
print(bonus_marks)  # to print the marks of all students after adding bonus marks

# Q-7 after bonus-> recalculate pass/fail
final_result = bonus_marks.apply(lambda x: 'Pass' if x > 40 else 'Fail')  # to recalculate pass/fail status 
print("Final result after adding bonus:")  # to print a message before the final result
print(final_result)  # to print the final pass/fail result

# Level: 4 Interview-Level Questions
# Q-8 find second highest marks
second_highest_marks = marks.nlargest(2).iloc[-1]  # to find the second highest marks
print("Second highest marks:")  # to print a message before the second highest marks
print(second_highest_marks)  # to print the second highest marks

# Q-9 Sort students by marks
sorted_marks = marks.sort_values(ascending=False)  # to sort the students by their marks in descending order
print("Students sorted by marks:")  # to print a message before the sorted list
print(sorted_marks)  # to print the sorted list of students by their marks

# Final interview question
# Q-10 find student who scored above average and passed(>40)
above_average_passed = marks[(marks > average_marks) & (marks > 40)]
print("Students who scored above average and passed:")  # to print a message before the list
print(above_average_passed)  # to print the marks of students who scored above average and passed