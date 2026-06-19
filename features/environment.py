import requests
from Python_QA_Framework.payloads.library_payloads import add_book_payload

BASE_URL = "http://216.10.245.166"
LIBRARY_DELETEBOOK = f"{BASE_URL}/Library/DeleteBook.php"

def after_scenario(context, scenario):
    # Delete a book
    delete_book_response = requests.post(
        LIBRARY_DELETEBOOK,
        json={"ID": context.book_ID},
        headers={"Content-Type": "application/json"},
    )
    delete_book_response_json = delete_book_response.json()
    print(delete_book_response_json["msg"])

    assert delete_book_response.status_code == 200

    # Check if 'msg' key exists in the response
    if "msg" in delete_book_response_json:
        assert delete_book_response_json["msg"] == "book is successfully deleted"