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

