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

# Check if the request was successful
if response.status_code == 200:
  # Get the HTML content
  html_content = response.text

  # Save the HTML content to a file (optional)
  with open("downloaded_page.html", "w") as f:
    f.write(html_content)

  # Print the first 100 characters of the HTML content
  print(html_content[:100])
else:
  print(f"Failed to download website. Status code: {response.status_code}")
