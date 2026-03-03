from sqlalchemy import create_engine
import pandas as pd

engine = create_engine("mysql+mysqlconnector://root:amp%409901@localhost/school")

# Read table into pandas
df = pd.read_sql("SELECT * FROM students", engine)
print(df)

# Average marks
print("Average Marks:", df["marks"].mean())

# Highest score
print("Highest Score Record(s):")
print(df[df["marks"] == df["marks"].max()])

# Average marks by subject
print("Average Marks by Subject:")
print(df.groupby("subject")["marks"].mean())