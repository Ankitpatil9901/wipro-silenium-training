
#DataFrame is a 2-dimensional labeled data structure (rows & columns), # like an Excel SQL tables
import pandas as pd
# Create DataFrame from List of Dictionaries
data = [
{"Name": "Ram", "Age":25},
{"Name": "Sam", "Age": 30},
{"Name": "John", "Age": 28}

]

df = pd.DataFrame(data)
print(df)

#create df from dictionary
s1 = pd.Series([1, 2, 3])
s2= pd.Series([4, 5, 6])
df = pd.DataFrame({"A": s1, "B": s2})
print(df)

#Create DataFrame from NumPy Array
import numpy as np
arr = np.array([[1, 2], [3, 4], [5, 6]])
df = pd.DataFrame (arr, columns=["A", "B"])
print (df)

#create df using csv
df = pd.read_csv("employees_data.csv")
print(df.head())
#create the empty df
df = pd.DataFrame()
print(df)


#Create DataFrame with Custom Index
data = {
"Name": ["Ram", "Sam"],
"Age" : [25, 30]
}
df = pd.DataFrame (data, index= ["Emp1", "Emp2"])
print(df)