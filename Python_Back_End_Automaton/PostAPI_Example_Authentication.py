import requests
import json
from Payload import *
from utilities.resources import *
from utilities.configurations import *

# Authentication
url_user = getGithubUrl("/user")
user, token = getCredentials()
github_response = requests.get(url_user, auth=(user, token))
print(github_response.status_code)
# print(github_response.headers)
# print(github_response.json())

url_repository = getGithubUrl("/user/repos")
repository_response = requests.get(url_repository, auth=(user,token))
print(repository_response.status_code)

# Use .session() to creat reusable HTTP client session
se = requests.Session()
se.auth = auth = (user,token)
repository_response2 = se.get(url_repository)
print(repository_response2.status_code)
