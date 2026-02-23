#Create a scalar variable ${NAME} and print it.
#Assign two numbers to variables and print their sum.
#Create a variable ${CITY} and use it inside a sentence.
#Reassign a variable value inside a test case and log the updated value.
#Create a list variable @{FRUITS} and print the first item.
#Loop through a list variable and print each element.
#Find the length of a list variable.
#Create a dictionary variable &{USER} and print one key value.
#Add a new key-value pair to a dictionary variable.
#Access dictionary values inside a loop and print key and value.
*** Settings ***
Library    BuiltIn
Library    Collections

*** Variables ***
${NAME}        Ankit
${NUM1}        10
${NUM2}        20
${CITY}        Kalaburagi

@{FRUITS}      Apple    Banana    Mango

&{USER}        username=admin    role=tester

*** Test Cases ***
Variable Practice Demo

    # 1. Print scalar variable
    Log    ${NAME}

    # 2. Print sum of two numbers
    ${sum}=    Evaluate    ${NUM1} + ${NUM2}
    Log    Sum of numbers is ${sum}

    # 3. Use variable inside sentence
    Log    I live in ${CITY}

    # 4. Reassign variable value
    ${CITY}=    Set Variable    Bangalore
    Log    Updated city is ${CITY}

    # 5. Print first list item
    Log    First fruit is ${FRUITS}[0]

    # 6. Loop through list
    FOR    ${fruit}    IN    @{FRUITS}
        Log    Fruit name is ${fruit}
    END

    # 7. Find list length
    ${length}=    Get Length    ${FRUITS}
    Log    Total fruits: ${length}

    # 8. Print dictionary value
    Log    Username is ${USER}[username]

    # 9. Add new key-value to dictionary
    Set To Dictionary    ${USER}    age=25
    Log    User age is ${USER}[age]

    # 10. Loop through dictionary
    FOR    ${key}    ${value}    IN    &{USER}
        Log    ${key} : ${value}
    END
