import json

with open("C://Users//Hp//PycharmProjects//PythonAdvanceProgram//dataformats//emploee.json" , 'r') as  file:
    data=json.load(file)

print(data)
print(data["name"])

with open("C://Users//Hp//PycharmProjects//PythonAdvanceProgram//dataformats//nestedjson.json" , 'r') as  file:
    data=json.load(file)

email = data["user"]["profile"]["email"]
print(email)




#writting to json file - dump method()
#writejson.json
data={
  "name": "Harsha",
  "role": "Tester",
  "experience": 5,
  "skills": ["Python", "Automation", "API"]
}

with open("C://Users//Hp//PycharmProjects//PythonAdvanceProgram//dataformats//writejson.json" , 'w') as  file:
    json.dump(data, file)


#update or modify the json file
#read the json file
# write it back to the file


with open("C://Users//Hp//PycharmProjects//PythonAdvanceProgram//dataformats//updatejson.json" , 'r') as  file:
    data= json.load(file)

#update the value
data["experience"]=6

with open("C://Users//Hp//PycharmProjects//PythonAdvanceProgram//dataformats//updatejson.json" , 'w') as  file:
    json.dump(data, file)


