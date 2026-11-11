import requests

url = 'https://jsonplaceholder.typicode.com/posts/1'
response = requests.get(url, timeout=10)
response.raise_for_status()
post = response.json()
print(post["id"], post["title"])

new = requests.post(
    'https://jsonplaceholder.typicode.com/posts',
    json={'title': 'hello', 'body': 'test', 'userId': 1},
    timeout=10,
)
print(new.status_code, new.json())