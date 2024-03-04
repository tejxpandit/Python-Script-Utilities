import requests
import time
import pickle
from bs4 import BeautifulSoup

URL = "https://www.nuailab.com/events/workshops/ai_winterschool2024/readtest.php"

html = requests.post(URL, headers={"User-Agent": "Tej Pandit"})

#print(html.text)

html_parser = BeautifulSoup(html.text, 'html.parser')

table = html_parser.find("table")

# Extract all rows
rows = table.find_all("tr")

