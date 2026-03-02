'''

Creating data

Selecting data

Filtering data

Cleaning data

Transforming columns

Aggregating data

Merging datasets

Exporting results
'''

import pandas as pd
# Creating data DFR using the dictionary

data = {

"Name": ["Ram", "Sam", "John", "Priya"],
"Age" :[25, 30, 28, 22],
"Salary": [40000, 50000, 45000, 38000]
}
df = pd.DataFrame(data)
print(df)

#Selecting single data
print(df["Age"])
#select multiple data or cols
print(df[["Age", "Name"]])
#select ros using loc and iloc
print(df.loc[0:2])#nth index
print(df.iloc[0:2])#n-1 index

#filtering based on the conditions
df = pd.DataFrame(data)
print(df)


#emp with salary >40000
filt = df[df["Salary"]>40000]
print(filt)
filtered = df[df["Salary"]<40000]
print(filtered)

#multiple conditions
filtered1 = df[(df["Salary"] > 40000) & (df["Age"] > 25)]
print(filtered1)

#Cleaning data -- adding or modifying the data
data = {
"Name": ["Ram", "Sam", "John", "Priya"],
"Salary": [40000, 50000, 45000, 38000]
}
df = pd.DataFrame(data)
#add the bonus cols
df["Bonus"]= df["Salary"]*0.10
print(df)

#modifying the current column - inc the sal
df["Salary"]= df["Salary"]+20000
print(df)

#Sorting data asc oe desc
data = {
"Name": ["Ram", "Sam", "John", "Priya"],
"Age" :[25, 30, 28, 22],
"Salary": [40000, 50000, 45000, 38000]
}
df = pd.DataFrame(data)

#Sort the salary in asc order

sorted_df = df.sort_values("Salary",ascending=True)
print(sorted_df)

#Sort the salary in desc order

sorted_df = df.sort_values("Salary",ascending=False)
print(sorted_df)

#handling the missing data
import numpy as np
data = {
"Name": ["Ram", "Sam", None],
"Age" :[25, np.nan, 22],
}
df = pd.DataFrame(data)
print("missing values")
print(df.isnull())

df_filled = df.fillna(0)
print(df_filled)

#drop missing rows
data = {
"Name": ["Ram", "Sam", None],
"Age" :[25, None, 22],
"Salary": [40000, 50000, None]
}
df = pd.DataFrame(data)
print(df)
df = df.dropna()
print(df)

#groupby

#GroupBy and Aggregation
data = {

"City": ["Delhi", "Mumbai", "Delhi", "Chennai"],
"Salary": [40000, 50000, 45000, 38000]
}
df = pd.DataFrame(data)
# average salary per city
result = df.groupby("City") ["Salary"].mean()
print (result)
#multiple aggregation
result = df.groupby("City") ["Salary"].agg (["mean", "sum", "count"])
print (result)


#Merging DataFrames
df1 = pd.DataFrame({
"ID": [1, 2],
"Name": ["Ram", "Sam"]
})
df2= pd.DataFrame({

"ID": [1, 2],
"Salary": [40000, 50000]
})
merged=pd.merge (df1, df2, on="ID", how = "inner")
print (merged)


data = {
"Name": ["Ram", "Sam", "Ram"],

"Salary": [40000, 50000, 40000]
}
df = pd.DataFrame(data)
print("Before removing duplicates:")
print(df)
df = df.drop_duplicates ()
print("After removing duplicates:")
print(df)

