from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
print("connected successully")

db = client["school"] #create a db
collection = db["students"]#create collection

students = [
    {"name": "Ravi", "subject": "os", "marks": 88},
    {"name": "Sneha", "subject": "dbms", "marks": 97},
    {"name": "Ram", "subject": "cn", "marks": 75}
]

collection.insert_many(students)
#print the data
for doc in collection.find():
    print(doc)
#update the data
collection.update_one(
    {"name": "Ravi"},
    {"$set":{"marks":95}}
)


#delete the data
collection.delete_one({"name":"Sneha"})

import pandas as pd
from CRUD import collection
from pymongo import MongoClient

data = list(collection.find())
df = pd.DataFrame(data)
print(df)

print(df["marks"].mean())
print(df[df["marks"] == df["marks"].max()])

print(df.groupby("subject")["marks"].mean())
