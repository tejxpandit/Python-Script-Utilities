# Python Webpage HTML Downloader
# Tej Pandit

import requests

url = "https://www.example.com"

# Send a GET request to the URL
try:
  response = requests.get(url)
except requests.exceptions.RequestException as e:
  print(f"Error downloading website: {e}")
  exit(1)

