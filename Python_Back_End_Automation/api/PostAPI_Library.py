import requests
from Python_Back_End_Automation.api.Payload import *

# API Configuration in file. There's also another way to set up global configurations, see properties.ini file.
BASE_URL = "http://216.10.245.166"
LIBRARY_ADDBOOK = f"{BASE_URL}/Library/Addbook.php"
LIBRARY_DELETEBOOK = f"{BASE_URL}/Library/DeleteBook.php"

# Add a book
addBook_response = requests.post(
    LIBRARY_ADDBOOK,
    # json={                                                # Including all data in here makes the code look messy
    #     "name": "My First Ontario Bird Book",
    #     "isbn": "1459507371",
    #     "aisle": "157",
    #     "author": "Jeffrey C. Domm"
    # },
    json=add_book_payload("aert34"),                                  # Writing all payload elsewhere and import to use makes code look clean, and made the data reusable. Here we are typing in a random isbn for unique results.
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
    LIBRARY_DELETEBOOK,
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

