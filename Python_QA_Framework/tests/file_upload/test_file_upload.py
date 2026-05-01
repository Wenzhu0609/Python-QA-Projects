from pathlib import Path

import requests

from Python_QA_Framework.utilities.config import get_httpbin_url, get_swagger_petstore_url

DATA_DIR = Path(__file__).resolve().parents[2] / "data" / "files"

httpbin_upload_url = get_httpbin_url("/post")
file_path = DATA_DIR / "test_upload.txt"

with open(file_path, "rb") as file:
    files = {"file": file}
    response = requests.post(httpbin_upload_url, files=files)

print(response.text)

response_data = response.json()
print(response_data)
server_received_content = response_data["files"]["file"]

assert server_received_content == "Hello, this is a test upload!"
print("Test Passed!")

# Swagger Petstore upload file
swagger_petstore_upload_url = get_swagger_petstore_url("/pet/9843217/uploadImage")
dog_pic_path = DATA_DIR / "dog.jpg"

with open(dog_pic_path, "rb") as dog_pic:
    files = {"file": dog_pic}
    dog_pic_response = requests.post(
        swagger_petstore_upload_url,
        files=files,
        timeout=5,
    )
    print(dog_pic_response.status_code)
    print(dog_pic_response.headers["Content-Type"])
    print(dog_pic_response.json())

    assert dog_pic_response.status_code == 200
    assert "File uploaded" in dog_pic_response.json()["message"]
