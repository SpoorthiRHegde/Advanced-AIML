import requests
from bs4 import BeautifulSoup

url = "https://www.example.com"
html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')

print("Page title:", soup.title.string)
