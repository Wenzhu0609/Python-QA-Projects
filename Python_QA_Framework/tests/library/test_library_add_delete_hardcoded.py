import requests

from Python_QA_Framework.payloads.library_payloads import add_book_payload

# API configuration in file. Another option is global configuration in properties.ini.
BASE_URL = "http://216.10.245.166"
LIBRARY_ADDBOOK = f"{BASE_URL}/Library/Addbook.php"
LIBRARY_DELETEBOOK = f"{BASE_URL}/Library/DeleteBook.php"

# Add a book
add_book_response = requests.post(
    LIBRARY_ADDBOOK,
    json=add_book_payload("aert34"),
    headers={"Content-Type": "application/json"},
)

add_book_response_json = add_book_response.json()
print(add_book_response_json)

# Check if 'ID' key exists in the response
if "ID" in add_book_response_json:
    book_id = add_book_response_json["ID"]
    print(f"Book ID: {book_id}")
else:
    print("Error: 'ID' key not found in response")
    print(f"Response: {add_book_response_json}")

# Delete a book
delete_book_response = requests.post(
    LIBRARY_DELETEBOOK,
    json={"ID": book_id},
    headers={"Content-Type": "application/json"},
)
delete_book_response_json = delete_book_response.json()
print(delete_book_response_json["msg"])

assert delete_book_response.status_code == 200

# Check if 'msg' key exists in the response
if "msg" in delete_book_response_json:
    assert delete_book_response_json["msg"] == "book is successfully deleted"
