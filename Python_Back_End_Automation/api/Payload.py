from utilities.configurations import get_query


# In order to achieve a cleaner looking code, instead of writing all the data details within the json parameter, we write payload in one place and use each accordingly
# Hardcoded request payload:
def add_book_payload(isbn):                       # isbn is entered from the test scripts
    body = {
        "name": "My First Ontario Bird Book",
        "isbn": isbn,                           # Instead of a fixed isbn number, we use a random isbn entered at test script to create unique book id
        "aisle": "157",
        "author": "Jeffrey C. Domm"
    }
    return body

# Build the request payload dynamically using data fetched from the MySQL database.
def build_payload_from_db(query):
    add_body = {}
    tp = get_query(query)
    add_body['name'] = tp[0]
    add_body['isbn'] = tp[1]
    add_body['aisle'] = tp[2]
    add_body['author'] = tp[3]
    return add_body