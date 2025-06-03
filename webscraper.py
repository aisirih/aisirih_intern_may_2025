import requests
from bs4 import BeautifulSoup


# Making a GET request
r = requests.get('https://www.google.com')

# check status code for response received
# success code - 200
print(r)

# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')

for link in soup.find_all("a"):
    print(link.get("href"))

#print(soup.prettify())
