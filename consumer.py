import requests

response = requests.get("http://35.206.76.195:8072/head?count=10")

# Check to see if the response request worked
if (response.status_code != 200):
    raise Exception(f'Response status code: {response.status_code}')

# View the JSON data in response
data = response.json()
print(data)
