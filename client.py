import requests

url = '127.0.0.1:8000/api/v1/books'

response = requests.get(url)

if response.status_code == 200:
    print(response.json())