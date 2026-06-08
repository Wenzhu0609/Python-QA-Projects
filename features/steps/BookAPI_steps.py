from behave import *
import requests
from Python_QA_Framework.payloads.library_payloads import add_book_payload

# Globally configured:
from Python_QA_Framework.utilities.api_resources import ApiResources
from Python_QA_Framework.utilities.config import get_config

# Add a book from payload - dynamic version:

# delete_book_url = get_config()["API"]["library_endpoint"] + ApiResources.delete_book


@given('the book details which needs to be added to the Library')       # Book details in one place
def step_impl(context):
    context.add_book_url = get_config()["API"]["library_endpoint"] + ApiResources.add_book
    context.payload = add_book_payload("aert58")
    context.headers = {"Content-Type": "application/json"}

   
   
    # BASE_URL = "http://216.10.245.166"
    # context.url = f"{BASE_URL}/Library/Addbook.php"
    # context.payload = add_book_payload("aert34")
    # context.headers = {"Content-Type": "application/json"}



@when('we execute the AddBook PostAPI method')     # Only run the method
def step_impl(context):
    context.add_book_response = requests.post(
    context.add_book_url,
    json=context.payload,
    headers=context.headers,
)
    # context.add_book_response = requests.post(
    #     context.url,
    #     json=context.payload,
    #     headers=context.headers,
    # )

@then('the book will be added successfully')        # Check if 'ID' key exists in the response
def step_impl(context):
    add_book_response_json = context.add_book_response.json()
    book_ID = add_book_response_json["ID"]
    print(add_book_response_json)
    print(book_ID)
    assert add_book_response_json["Msg"] == "successfully added"

    # if "ID" in add_book_response_json:
    #     book_id = add_book_response_json["ID"]
    #     print(f"Book ID: {book_id}")
    # else:
    #     print("Error: 'ID' key not found in response")
    #     print(f"Response: {add_book_response_json}")
    
