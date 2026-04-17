import requests
import json

url = 'https://httpbin.org/post'
file_path = 'Python_Back_End_Automaton/test_upload.txt'
with open(file_path, 'rb') as f:
    files = {'file':f}
    r=requests.post(url,files=files)
print(r.text)

response_data = r.json()
print(response_data)
server_received_content = response_data['files']['file']

assert server_received_content == "Hello, this is a test upload!"
print('✅ Test Passed!')