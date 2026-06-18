import pandas as pd

# joins example
df1 = pd.DataFrame({
    'CustomerID': [1, 2, 3],
    'Name': ['Alice', 'Bob', 'Charlie']
})
df2 = pd.DataFrame({
    'CustomerID': [2, 3, 4],    
    'City': ['New York', 'Los Angeles', 'Chicago']
})
# inner join
inner_join = pd.merge(df1, df2, on='CustomerID', how='inner')
print("Inner Join:")
print(inner_join)
# left join
left_join = pd.merge(df1, df2, on='CustomerID', how='left')
print("\nLeft Join:")
print(left_join)
# right join
right_join = pd.merge(df1, df2, on='CustomerID', how='right')
print("\nRight Join:")
print(right_join)
# outer join
outer_join = pd.merge(df1, df2, on='CustomerID', how='outer')
print("\nOuter Join:")
print(outer_join)