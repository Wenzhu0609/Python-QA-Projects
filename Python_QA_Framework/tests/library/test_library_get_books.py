import requests

from Python_QA_Framework.utilities.config import get_config

get_book_url = get_config()["API"]["library_endpoint"] + "/Library/GetBook.php"

response = requests.get(
    get_book_url,
    params={"AuthorName": "Fannie Flagg"},
)

# The .json() method converts the response body into Python data.
json_response = response.json()
print(type(json_response))
print(json_response)

# Check response status code and content type:
assert response.status_code == 200
print(response.headers)
assert response.headers["content-type"] == "application/json;charset=UTF-8"

# Retrieve the book details with ISBN RGHCC
response2 = requests.get(
    get_book_url,
    params={"AuthorName": "rahulshetty"},
)
json_response2 = response2.json()
actual_book = None

for book in json_response2:
    if book["isbn"] == "RGHCC":
        actual_book = book
        break

assert actual_book is not None, "Book not found"
assert actual_book["isbn"] == "RGHCC", "ISBN mismatch"
assert actual_book["book_name"] == "Pythonselenium 18 hrs by Rahulshetty", "Title mismatch"
