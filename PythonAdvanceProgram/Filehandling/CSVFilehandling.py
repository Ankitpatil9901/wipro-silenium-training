import csv
#reading the csv file
with open("C://Users//Hp//PycharmProjects//PythonAdvanceProgram//dataformats//data.csv","r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# que 1.1.Handle FileNotFoundError Exception When Opening a File
try:
    with open("C://Users//Hp//PycharmProjects//PythonAdvanceProgram//dataformats//data15.csv", "r") as file:
        data= file.read()
except FileNotFoundError:
    print("File missing")
else:
    print("File found")


#writting the csv file
with open("C://Users//Hp//PycharmProjects//PythonAdvanceProgram//dataformats//write.csv","w", newline="")as file:
    writer = csv.writer(file)
    writer.writerow(["id","name","marks"])
    writer.writerow([1,"Rahul",85])
    writer.writerow([2, "Amit", 87])

#append the data to csv file
with open("C://Users//Hp//PycharmProjects//PythonAdvanceProgram//dataformats//data.csv","w", newline="")as file:
    writer = csv.writer(file)
    writer.writerow([3,"kiran",88])

