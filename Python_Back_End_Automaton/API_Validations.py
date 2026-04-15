import requests
import json

response = requests.get('http://216.10.245.166/Library/GetBook.php', 
             params={"AuthorName":"Fannie Flagg"},)

# The step by step way:
# print(response.text)
# print(type(response.text))
# dict_resposne = json.loads(response.text)     #.loads generates a library, and in our case, the resposne is a list, so Python got confused and did an extra step to convert it into a list.
# print(type(dict_resposne))
# print(dict_resposne[0]['isbn'])

# The open with .json method:
json_response = response.json()     # .json() automatically did all the 'resposne.text', json.loads(response.text), and converting in one step
print(type(json_response))
print(json_response[0]['isbn'])

# Check resposne status code:
assert response.status_code == 200
# To verify if the content type is json application:
print(response.headers)     # This information is within the header, so we need to extract contents of the headers first, which is in a dictionary format
assert response.headers['content-type'] == 'application/json;charset=UTF-8'

# Retireve the book details with ISBN RGHCC
response2 = requests.get('http://216.10.245.166/Library/GetBook.php', 
             params={"AuthorName":"rahulshetty"},)
json_response2 = response2.json()
for book in json_response2:
    if book['isbn'] == 'RGHCC':
        actualBook = book
        break

assert actualBook is not None, "Book not found"
assert actualBook['isbn'] == 'RGHCC', "ISBN mismatch"
assert actualBook['book_name'] == 'Pythonselenium 18 hrs by Rahulshetty', "Title mismatch"
