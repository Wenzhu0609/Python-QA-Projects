import requests
from utilities.configurations import *


# http://rahulshettyacademy.com
# to track the month of visit, it uses cookies 'visit-month'


# Send any cookies in a dictionary format
rsa_cookie = {'visit-month':'February'}
rsa_url = get_rsa_url()

rsa_response = requests.get(rsa_url,cookies=rsa_cookie)
# print(rahulshetty_response.status_code)
assert rsa_response.status_code == 200

se = requests.Session()
se.cookies.update({'visit-month':'February'})

# To check if the cookie sent was actually accepted by the server:
httpbin_cookie = {'visit-year':'2022'}
httpbin_url_cookies = get_httpbin_url("/cookies")
httpbin_response = se.get(httpbin_url_cookies, cookies=httpbin_cookie)
print(httpbin_response.text)
httpbin_response_json = httpbin_response.json()
assert "cookies" in httpbin_response_json, "Response does not contain 'cookies'."
assert "visit-year" in httpbin_response_json['cookies'], "Cookie 'visit-year' was not returned by the server."
assert httpbin_response_json["cookies"]["visit-year"] == "2022", "Cookies 'visit-year' value is incorrect."
assert "visit-month" in httpbin_response_json['cookies'], "Cookie 'visit-month' was not returned by the server."
assert httpbin_response_json["cookies"]["visit-month"] == "February", "Cookies 'visit-year' value is incorrect."
