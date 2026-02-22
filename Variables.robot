*** Settings ***

Library     SeleniumLibrary

*** Variables ***
# A scalar variable can only contain one value -$
# A list Variable can contain multiple values -@
# A dictionary variable can contain multiple key value pairs &

${name}         Ankit
${city}         Kalaburagi
${address}      Sangameshwar colony

@{list1}        red        white        green
@{list2}        apple      grapes       watermelon

&{creds}        username=admin    password=admin123

*** Test Cases ***
Verify the variables
    Log     ${name}
    Log     ${city}
    Log     ${address}

    FOR    ${element}    IN    @{list1}
        Log    ${element}
    END

    FOR    ${element}    IN    @{list2}
        Log    ${element}
    END

    Log     ${list1}[0]
    Log     ${list1}[1]
    Log     ${creds}[username]
    Log     ${creds}[password]
