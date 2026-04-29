import requests
from Python_Back_End_Automation.utilities.configurations import get_httpbin_url, get_swagger_petstore_url


httpbin_upload_url = get_httpbin_url('/post')
file_path = 'Python_Back_End_Automation/data/files/test_upload.txt'
with open(file_path, 'rb') as f:
    files = {'file':f}
    r=requests.post(httpbin_upload_url,files=files)
print(r.text)

response_data = r.json()
print(response_data)
server_received_content = response_data['files']['file']

assert server_received_content == "Hello, this is a test upload!"
print('✅ Test Passed!')


# Swagger Petstore upload file
swagger_petstore_upload_url = get_swagger_petstore_url('/pet/9843217/uploadImage')
dog_pic_path = 'Python_Back_End_Automation/data/files/dog.jpg'
with open(dog_pic_path, 'rb') as dog_pic:
    files = {'file': dog_pic}
    r_dog_pic = requests.post(swagger_petstore_upload_url, files=files, timeout = 5)
    print(r_dog_pic.status_code)
    print(r_dog_pic.headers["Content-Type"])
    print(r_dog_pic.json())
    assert r_dog_pic.status_code == 200
    assert "File uploaded" in r_dog_pic.json()['message']
