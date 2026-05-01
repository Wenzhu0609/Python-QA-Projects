import requests
from Python_QA_Framework.utilities.config import get_httpbin_url, get_rsa_url


def test_cookies():
    # http://rahulshettyacademy.com tracks the month of visit with the
    # "visit-month" cookie.
    rsa_cookie = {'visit-month': 'February'}
    rsa_url = get_rsa_url()

    rsa_response = requests.get(rsa_url, cookies=rsa_cookie)
    assert rsa_response.status_code == 200

    session = requests.Session()
    session.cookies.update({'visit-month': 'February'})

    # Check if the cookie sent was accepted by the server.
    httpbin_cookie = {'visit-year': '2022'}
    httpbin_url_cookies = get_httpbin_url("/cookies")
    httpbin_response = session.get(httpbin_url_cookies, cookies=httpbin_cookie)
    print(httpbin_response.text)

    httpbin_response_json = httpbin_response.json()
    assert "cookies" in httpbin_response_json, "Response does not contain 'cookies'."
    assert "visit-year" in httpbin_response_json['cookies'], "Cookie 'visit-year' was not returned by the server."
    assert httpbin_response_json["cookies"]["visit-year"] == "2022", "Cookie 'visit-year' value is incorrect."
    assert "visit-month" in httpbin_response_json['cookies'], "Cookie 'visit-month' was not returned by the server."
    assert httpbin_response_json["cookies"]["visit-month"] == "February", "Cookie 'visit-month' value is incorrect."


if __name__ == "__main__":
    test_cookies()
