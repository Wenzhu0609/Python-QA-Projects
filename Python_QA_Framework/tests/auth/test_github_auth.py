import requests

from Python_QA_Framework.utilities.config import get_github_credentials, get_github_url

# Authentication
url_user = get_github_url("/user")
user, token = get_github_credentials()
github_response = requests.get(url_user, auth=(user, token))
assert github_response.status_code == 200

url_repository = get_github_url("/user/repos")
repository_response = requests.get(url_repository, auth=(user, token))
assert repository_response.status_code == 200

# Use .session() to create reusable HTTP client session.
session = requests.Session()
session.auth = (user, token)
repository_response2 = session.get(url_repository)
assert repository_response2.status_code == 200
