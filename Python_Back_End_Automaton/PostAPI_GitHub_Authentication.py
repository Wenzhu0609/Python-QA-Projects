import requests
import json
from Payload import *
from utilities.resources import *
from utilities.configurations import get_github_url, get_github_credentials

# Authentication
url_user = get_github_url("/user")
user, token = get_github_credentials()
github_response = requests.get(url_user, auth=(user, token))
# print(github_response.status_code)
assert github_response.status_code == 200
# print(github_response.headers)
# print(github_response.json())

url_repository = get_github_url("/user/repos")
repository_response = requests.get(url_repository, auth=(user,token))
# print(repository_response.status_code)
assert repository_response.status_code == 200

# Use .session() to creat reusable HTTP client session
se = requests.Session()
se.auth = auth = (user,token)
repository_response2 = se.get(url_repository)
# print(repository_response2.status_code)
assert repository_response2.status_code == 200
