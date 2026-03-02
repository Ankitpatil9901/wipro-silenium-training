import pandas as pd
import numpy as np

#1. Create a DataFrame containing missing (None/NaN) values
data = {
    "Name": ["Ram", "Sam", "John", "Priya", "Anita", None],
    "Age": [25, np.nan, 28, 22, 30, 27],
    "Salary": [40000, 50000, None, 38000, 60000, 45000],
    "Department": ["Finance", "HR", "IT", "Marketing", "IT", "HR"],
    "City": ["Mumbai", "Bangalore", "Bangalore", "Delhi", None, "Bangalore"]
}

df = pd.DataFrame(data)
print("1.Original DataFrame with missing values:\n", df)

# 2️.Detect missing values
print("2.Missing values:", df.isnull())
print( df.isnull().sum())

# 3️. Replace missing values with 0
df_filled = df.fillna({
    "Age": 0,
    "Salary": 0,
    "Name": "Unknown",
    "City": "Unknown"
})
print("3.replacing missing values with 0:", df_filled)

# 4️. Drop rows containing missing values
df_dropped = df.dropna()
print("4.Df after dropping rows with missing values:", df_dropped)

# 5️.Sort the DataFrame by Age in ascending order
df_sorted_age = df.sort_values(by="Age")
print("5.Df sorted by Age (ascending):", df_sorted_age)

# 6️.Sort the DataFrame by Salary in descending order
df_sorted_salary = df.sort_values(by="Salary", ascending=False)
print("6. DataFrame sorted by Salary (descending):", df_sorted_salary)

# 7️.Group by Department and find average Salary per department
avg_salary = df.groupby("Department")["Salary"].mean()
print("7. Avg Salary per Dept:\n", avg_salary)

# 8️.Find total Salary per department using groupby
total_salary = df.groupby("Department")["Salary"].sum()
print("8.Total Salary per Dept:", total_salary)

# 9️. Filter employees where Age > 25 AND City = 'Bangalore'
filtered = df[(df["Age"] > 25) & (df["City"] == "Bangalore")]
print("9.Employees with Age > 25 AND City = 'Bangalore':", filtered)

# 10. Create a new column 'Tax' which is 10% of Salary using apply()
df["Tax"] = df["Salary"]*0.10
print("10.Df with Tax column (10% of Salary):\n", df)