import requests
from Python_QA_Framework.utilities.config import get_rsa_url


def test_redirect_behaviour():
    rsa_url = get_rsa_url()

    redirect_response = requests.get(rsa_url, allow_redirects=False)
    assert redirect_response.status_code in [301, 302, 307, 308]
    assert "Location" in redirect_response.headers
    assert redirect_response.headers["Location"].startswith("https://")

    final_response = requests.get(rsa_url)
    assert final_response.status_code == 200
    assert len(final_response.history) > 0
    assert final_response.url.startswith("https://")

    print("Redirect test passed.")

if __name__ == "__main__":
    test_redirect_behaviour()
