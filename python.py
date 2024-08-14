import requests
from bs4 import BeautifulSoup

url = 'https://www.google.com/search?q=w3schools&oq=w3schools&gs_lcrp=EgZjaHJvbWUyDwgAEEUYORiDARixAxiABDINCAEQABiDARixAxiABDINCAIQABiDARixAxiABDINCAMQABiDARixAxiABDINCAQQABiDARixAxiABDIQCAUQABiDARixAxiABBiKBTINCAYQABiDARixAxiABDIGCAcQBRhA0gEIMTkxOGowajeoAgiwAgE&sourceid=chrome&ie=UTF-8'  
response = requests.get(url)

if response.status_code == 200:
    print("Successfully fetched the webpage!")
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

soup = BeautifulSoup(response.text, 'html.parser')

title = soup.title.text
print(f"Page title: {title}")
print("Sucessfully fetched the title of the webpages using BeautifulSoup4 and requests")
