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

# Extract content from each row
for row in rows:
    # Extract data cells (can be "td" or "th")
    cells = row.find_all("td")
    
    # Extract and print content from each cell
    for cell in cells:
        content = cell.text.strip()  # Remove leading/trailing whitespace
        print(content, end=" ")  # Print each cell content with a space
    print()  # Print a newline after each row

