import requests
import json
from Payload import *
from utilities.resources import *
from utilities.configurations import *

# Authentication
url = getConfig()['API']['github_endpoint']
user, token = getCredentials()
github_response = requests.get(url, auth=(user, token))
print(github_response.status_code)
print(github_response.headers)
print(github_response.json())
