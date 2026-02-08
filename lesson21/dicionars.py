student_data = {
    "id1":{
        "name":"Aziz",
        "class":"VII",
        "subject":"Math"
    },
    "id2":{
        "name":"Shock",
        "class":"VII",
        "subject":"Math"
    },
    "id3":{
        "name":"Sonic",
        "class":"VII",
        "subject":"Math"
    },
    "id4":{
        "name":"Aziz",
        "class":"VII",
        "subject":"Math"
    },
}

result = {}
for key , value in student_data.items():
    if value not in result.values():
        result[key]=value
print(result)