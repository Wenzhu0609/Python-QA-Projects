from Python_QA_Framework.utilities.db_utils import get_query


# In order to achieve cleaner-looking code, instead of writing all the data
# details within the json parameter, we write payload in one place and reuse it.
# Hardcoded request payload:
def add_book_payload(isbn):
    body = {
        "name": "My First Ontario Bird Book",
        "isbn": isbn,
        "aisle": "157",
        "author": "Jeffrey C. Domm"
    }
    return body


# Build the request payload dynamically using data fetched from the MySQL database.
def build_payload_from_db(query):
    add_body = {}
    tp = get_query(query)
    add_body["name"] = tp[0]
    add_body["isbn"] = tp[1]
    add_body["aisle"] = tp[2]
    add_body["author"] = tp[3]
    return add_body
