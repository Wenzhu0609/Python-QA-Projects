import json

courses = '{"name": "JohnReese",  "languages": ["Java", "Python"]}'

# Loads method parses JSON string and returns in a dictonary


dict_courses = json.loads(courses)
print(type(dict_courses))
print(dict_courses["name"])
print(dict_courses["languages"])

# Step by step way to extract the 1st item in the list
# list_languages = dict_courses['languages']
# print(type(list_languages))
# print(list_languages[0])

# How to write it in one line:
print(dict_courses['languages'][0])

# Parse content presnet in JSON file

with open('Python_Back_End_Automation/data/Course.json') as f1:
    data1 = json.load(f1)
    print(data1)
    print(type(data1))
    print(data1["courses"][1])   # Print the content of the 2nd course
    print(data1['courses'][1]['title'])
    print(data1['dashboard']['website'])
# Price of the course "RPA" without depending on index
    data1['courses']
    for course in data1['courses']:
        if course['title'] == 'RPA':
            course_price = course['price']
            print(f"Course price is ${course_price}.")
            assert course_price == 45                   # To validate the JSON file returned the correct info

# To compare 2 JSON Shcemas using Python dicrionaries
with open('Python_Back_End_Automation/data/Course1.json') as f2:
    data2 = json.load(f2)
    assert data1 == data2


