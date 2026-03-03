import pandas as pd
from click.testing import Result

# reading a csv file using pandas
df = pd.read_csv("student_data.csv")
print(df)

# Create Avg Marks
df['Avg Marks'] = (df['Math'] + df['Science'] + df['English'])/3
print(df)

# Create Result column:
# Pass if Average >= 70
# Fail otherwise

df['Result'] = df['Avg Marks'].apply(lambda x: 'Pass' if x >= 70 else 'Fail')

#What is the average score per subject?

print(df[['Math','Science','English']].mean())
#Does attendance correlate with performance?
print(df['Attendance'].corr(df['Avg Marks']))
#Compare performance by gender.
print(df.groupby('Gender')['Avg Marks'].mean())
#How many students passed vs failed?
print(df['Result'].value_counts())

#-------------------- Visualisation---------------------------------------

import matplotlib.pyplot as plt

# Bar chart -- Average subject scores
avg_scores = df[['Math','Science','English']].mean()
avg_scores.plot(kind='bar')
plt.title("Average Subject Scores")
plt.xlabel("Subjects")
plt.ylabel("Average Marks")
plt.show()


# Scatter plot -- Attendance vs Average Marks
plt.scatter(df['Attendance'], df['Avg Marks'])
plt.title("Attendance vs Average Marks")
plt.xlabel("Attendance")
plt.ylabel("Average Marks")
plt.show()


# Boxplot -- Marks distribution by Gender
df.boxplot(column='Avg Marks', by='Gender')
plt.title("Marks Distribution by Gender")
plt.xlabel("Gender")
plt.ylabel("Average Marks")
plt.suptitle("")
plt.show()


# Pie chart -- Pass vs Fail
result = df['Result'].value_counts()
result.plot(kind='pie', autopct='%1.1f%%')
plt.title("Pass vs Fail")
plt.ylabel("")
plt.show()