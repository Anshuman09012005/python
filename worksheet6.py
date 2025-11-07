
import scipy as sp
import pandas as pd
#Q1
print(sp.__version__)
print(pd.__version__)

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)
print("\nCreated DataFrame:")
print(df)

#Q2
s1 = pd.Series([100, 200, 300, 400, 500])
print("2.1 S1 Series:")
print(s1)
print("\n")
second_element = s1.iloc[1]
fourth_element = s1.iloc[3]
print("2.2 Second and fourth elements:")
print(f"Second element: {second_element}")
print(f"Fourth element: {fourth_element}")
print("\n")
s2 = pd.Series([10, 20, 30, 40, 50])
addition_result = s1 + s2
print("2.3 Result of S1 + S2:")
print(addition_result)


#Q3
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'London', 'Paris']}
df = pd.DataFrame(data)
print("3.1 'Name' and 'City' columns:")
print(df[['Name', 'City']])
df['Salary'] = [50000, 60000, 70000]
print("\n3.2 DataFrame after adding 'Salary' column:")
print(df)
average_age = df['Age'].mean()
total_salary = df['Salary'].sum()
print(f"\n3.3 Basic Statistics:")
print(f"Average Age: {average_age}")
print(f"Total Sum of Salary: {total_salary}")

#Q4
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'Age': [25, 30, 35, 28, 22],
        'City': ['New York', 'London', 'Paris', 'Tokyo', 'Sydney']}
df = pd.DataFrame(data)
filtered_df = df[df['Age'] > 28]
print("Filtered DataFrame (Age > 28):")
print(filtered_df)

#Q5
csv_data = """Name,Department,Salary
John,Sales,50000
Jane,Marketing,60000
Emily,HR,55000"""
df = pd.read_csv(import.StringIO(csv_data))
print("Original DataFrame:")
print(df)
filtered_df = df[df['Salary'] > 55000]
print("\nFiltered rows (Salary > 55000) - Name and Department columns:")
print(filtered_df[['Name', 'Department']])

#Q6
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'Department': ['HR', 'IT', 'HR', 'Finance', 'IT'],
        'Salary': [60000, 75000, 62000, 80000, 78000]}
df = pd.DataFrame(data)
average_salary_by_department = df.groupby('Department')['Salary'].mean()
print("Average Salary by Department:")
print(average_salary_by_department)


#Q7
df1 = pd.DataFrame({
    'Name': ['John', 'Jane', 'Emily'],
    'Department': ['Sales', 'Marketing', 'HR']
})
df2 = pd.DataFrame({
    'Name': ['John', 'Jane', 'Emily'],
    'Experience (Years)': [5, 7, 3]
})
merged_df = pd.merge(df1, df2, on='Name')
print(merged_df)


#Q8
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Experience (Years)': [5, 10, 3, 8],
        'Salary': [60000, 80000, 45000, 75000]}
df = pd.DataFrame(data)
sorted_df = df.sort_values(by='Experience (Years)', ascending=False)
print(sorted_df)