import requests

response_data = requests.get('https://httpbin.org/ip').json()
print(f'My IP is {response_data["origin"]}')

