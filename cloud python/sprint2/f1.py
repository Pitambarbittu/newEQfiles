import requests

import json

api_url="http://jsonplaceholder.typicode.com/todos"

todos_id={"userId":1, "title":"data added", "completed":True}
print(type(todos_id))
response=requests.post(api_url, json=todos_id)

print(response)
print(response.json())
print(response.headers["content-type"])


api_url="http://jsonplaceholder.typicode.com/todos"

todos_id={"userId":1, "title":"data added", "completed":False}
print(type(todos_id))
head={'content-type':'application/json'}
response=requests.post(api_url, data=json.dumps(todos_id), headers=head)

print(response)
print(response.json())
print(response.headers)


BASE_URL="http://jsonplaceholder.typicode.com/todos/10"
response=requests.get(BASE_URL)
print(response)
print(response.json())

todos_id={"userId":3, "title":"put data", "completed":False}
response=requests.patch(BASE_URL, json=todos_id)
print(response.json())

todos_id={"Title":"Testing"}
response=requests.put(BASE_URL, todos_id)
print(response.json())
print(response)

response=requests.delete(BASE_URL)
print(response.json)


