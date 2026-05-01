import requests

from Python_QA_Framework.payloads.library_payloads import build_payload_from_db
from Python_QA_Framework.utilities.api_resources import ApiResources
from Python_QA_Framework.utilities.config import get_config

add_book_url = get_config()["API"]["library_endpoint"] + ApiResources.add_book
delete_book_url = get_config()["API"]["library_endpoint"] + ApiResources.delete_book

headers = {"Content-Type": "application/json"}

# Add a book from payload - dynamic version:
query = "select * from Books"
add_book_response = requests.post(
    add_book_url,
    json=build_payload_from_db(query),
    headers=headers,
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
    delete_book_url,
    json={"ID": book_id},
    headers=headers,
)
delete_book_response_json = delete_book_response.json()
print(delete_book_response_json["msg"])

assert delete_book_response.status_code == 200

# Check if 'msg' key exists in the response
if "msg" in delete_book_response_json:
    assert delete_book_response_json["msg"] == "book is successfully deleted"
else:
    print("Error: 'msg' key not found in delete response")
    print(f"Response: {delete_book_response_json}")
