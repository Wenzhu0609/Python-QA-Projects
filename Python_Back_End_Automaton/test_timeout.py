import requests
from utilities.configurations import get_rsa_url

# To avoid waiting forever for the server to respond, we set timeout value to let it give up the request once reach the waiting limit.

rsa_url = get_rsa_url()
response = requests.get(rsa_url, allow_redirects=False, timeout=2)

print(response.status_code)

# Do not wait over 5s, but for this test to pass, the API response time should normally be under 3s.
timeout_response = requests.get(rsa_url, timeout=5)
assert timeout_response.status_code == 200
assert timeout_response.elapsed.total_seconds() < 3