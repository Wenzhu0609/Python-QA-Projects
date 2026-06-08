from behave import *
import requests
from Python_QA_Framework.payloads.library_payloads import add_book_payload
from Python_QA_Framework.utilities.api_resources import ApiResources
from Python_QA_Framework.utilities.config import get_config


@given('the book details which needs to be added to the Library')       # Book details in one place
def step_impl(context):
    context.add_book_url = get_config()["API"]["library_endpoint"] + ApiResources.add_book
    context.payload = add_book_payload("aert58")
    context.headers = {"Content-Type": "application/json"}

@when('we execute the AddBook PostAPI method')     # Only run the method
def step_impl(context):
    context.add_book_response = requests.post(
    context.add_book_url,
    json=context.payload,
    headers=context.headers,
)

@then('the book will be added successfully')        # Check if 'ID' key exists in the response
def step_impl(context):
    add_book_response_json = context.add_book_response.json()
    book_ID = add_book_response_json["ID"]
    print(add_book_response_json)
    print(book_ID)
    assert add_book_response_json["Msg"] == "successfully added"
