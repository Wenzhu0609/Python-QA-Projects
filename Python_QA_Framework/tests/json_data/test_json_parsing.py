import json
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[2] / "data"

courses = '{"name": "JohnReese",  "languages": ["Java", "Python"]}'

# Loads method parses JSON string and returns a dictionary.
dict_courses = json.loads(courses)
print(type(dict_courses))
print(dict_courses["name"])
print(dict_courses["languages"])

# How to write it in one line:
print(dict_courses["languages"][0])

# Parse content present in JSON file.
with open(DATA_DIR / "Course.json") as file1:
    data1 = json.load(file1)
    print(data1)
    print(type(data1))
    print(data1["courses"][1])
    print(data1["courses"][1]["title"])
    print(data1["dashboard"]["website"])

    # Price of the course "RPA" without depending on index.
    for course in data1["courses"]:
        if course["title"] == "RPA":
            course_price = course["price"]
            print(f"Course price is ${course_price}.")
            assert course_price == 45

# To compare 2 JSON schemas using Python dictionaries.
with open(DATA_DIR / "Course1.json") as file2:
    data2 = json.load(file2)
    assert data1 == data2
