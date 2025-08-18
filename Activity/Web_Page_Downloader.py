import requests

url = "https://www.example.com"
response = requests.get(url)

print("Status Code:", response.status_code)
print("First 200 characters of content:")
print(response.text[:200])
