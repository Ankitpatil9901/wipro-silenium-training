import mysql.connector

#create th connection to my sql
connection=mysql.connector.connect(
    host = "localhost",
    username = "root",
    password = "amp@9901"
)
#connection.cursor() is a method used in python db drivers
# to create a cursor from an established db connection
cursor = connection.cursor()
print("Connected succesfully")
#create db
cursor.execute("CREATE DATABASE IF NOT EXISTS school")
connection.commit()
#Now reconnect with db
connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "amp@9901",
    database = "school"
)
cursor = connection.cursor()
print("Connected succesfully")
#create table
cursor.execute('''
CREATE TABLE IF NOT EXISTS students(
studentid INT AUTO_INCREMENT PRIMARY KEY,
studentname VARCHAR(50),
subject VARCHAR(50),
marks INT
)
''')

connection.commit()

#Insert data
query = "INSERT INTO students (studentname, subject, marks) VALUES (%s, %s, %s)"
values = ("Amul", "DSA", 98)

cursor.execute(query, values)
connection.commit()

#Insert multiple values
students_data = [
    ("Ravi","os",88),
    ("Sneha","dbms",97),
    ("Ram","cn",75)
]

cursor.executemany(query, students_data)
connection.commit()

#read data
cursor.execute("Select * from students")
rows = cursor.fetchall()

#update data
cursor.execute("Update students SET marks=95 where studentname='Amul'")
connection.commit()

#dalete data
cursor.execute("Delete from students  where studentname='Sneha'")
connection.commit()


