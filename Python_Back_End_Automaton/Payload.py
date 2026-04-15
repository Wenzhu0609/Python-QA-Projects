# In order to achieve a cleaner looking code, instead of writing all the data details within the json parameter, we write payload in one place and use each accordingly

def addBookPayload(isbn):                       # isbn is entered from the test scripts
    body = {
        "name": "My First Ontario Bird Book",
        "isbn": isbn,                           # Instead of a fixed isbn number, we use a random isbn entered at test script to create unique book id
        "aisle": "157",
        "author": "Jeffrey C. Domm"
    }
    return body
