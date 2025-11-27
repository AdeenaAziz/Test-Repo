import requests
from bs4 import BeautifulSoup #'''BeautifulSoup is a tool that helps Python: read website HTML find things inside it (links, text, images)'''

# Step 1: Get the website HTML
response = requests.get("https://www.netflix.com") 

# Step 2: Parse the HTML using BeautifulSoup, #"Take the website HTML and put it inside a variable called soup."
soup = BeautifulSoup(response.text, "html.parser")

# Step 3: Extract all links on the page
links = [a['href'] for a in soup.find_all('a', href=True)]

print(links)
