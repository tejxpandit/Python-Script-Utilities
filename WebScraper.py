import requests
import time
import pickle

URL_template = "https://www.fanfiction.net/s/14205444/1/Enchanting-Melodies"

# Generate List of URLs
chapters = 191 #191
chapter_urls = []
for c in range(chapters):
    url = URL_template + str(c+1) # added 1 for offset (no chapter 0)
    chapter_urls.append(url)
    #print(url)

# Get URL HTML
chapter_htmls = []
for c in range(chapters):
    html = requests.get(chapter_urls[c])
    chapter_htmls.append(html.text)
    time.sleep(1) # to prevent DDOS lock from websites detecting bots / IP traffic
    #print(html.text)

# Write HTML to pickle file
with open("temp\html_list", "wb") as fp:
    pickle.dump(chapter_htmls, fp)
