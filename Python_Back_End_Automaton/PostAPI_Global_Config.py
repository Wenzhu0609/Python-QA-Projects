import json
import configparser         # the defult package available in Python
from Payload import *
from utilities.configurations import *

import requests

# Utilizing global configuration:

# Add a book
addBook_response = requests.post(
    getConfig()['API']['endpoint']+'/Library/Addbook.php',
    json=addBookPayload("aert34"),
    headers={"Content-Type": "application/json"}
)

addBook_response_json = addBook_response.json()
print(addBook_response_json)

# Check if 'ID' key exists in the response
if 'ID' in addBook_response_json:
    bookID = addBook_response_json['ID']
    print(f"Book ID: {bookID}")
else:
    print("Error: 'ID' key not found in response")
    print(f"Response: {addBook_response_json}")


# Delete a book
deleteBook_response = requests.post(
    getConfig()['API']['endpoint']+'/Library/DeleteBook.php',
    json= {
        "ID": bookID
    },
    headers= {"Content-Type": "application/json"},
)
deleteBook_response_json = deleteBook_response.json()
print(deleteBook_response_json['msg'])

assert deleteBook_response.status_code == 200

# Check if 'msg' key exists in the response
if 'msg' in deleteBook_response_json:
    assert deleteBook_response_json['msg'] == "book is successfully deleted"

