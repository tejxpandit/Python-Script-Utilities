import requests
import time
import pickle
from bs4 import BeautifulSoup

URL = "https://www.nuailab.com/events/workshops/ai_winterschool2024/readtest.php"

html = requests.post(URL, headers={"User-Agent": "Tej Pandit"})

