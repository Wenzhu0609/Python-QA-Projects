from Python_Back_End_Automation.api.Payload import *
from utilities.configurations import *
from utilities.resources import *

import requests

# Utilizing global configuration:
addBook_url = get_config()['API']['library_endpoint'] + ApiResources.addBook
deleteBook_url = get_config()['API']['library_endpoint'] + ApiResources.deleteBook

headers={"Content-Type": "application/json"}
# Add a book
addBook_response = requests.post(addBook_url, json=addBookPayload("aert34"), headers=headers)

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
deleteBook_response = requests.post(deleteBook_url, json= {"ID": bookID}, headers=headers,)
deleteBook_response_json = deleteBook_response.json()
print(deleteBook_response_json['msg'])

assert deleteBook_response.status_code == 200

# Check if 'msg' key exists in the response
if 'msg' in deleteBook_response_json:
    assert deleteBook_response_json['msg'] == "book is successfully deleted"
else:
    print("Error: 'msg' key not found in delete response")
    print(f"Response: {deleteBook_response_json}")