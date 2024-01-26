import pickle
from bs4 import BeautifulSoup

# IMP : First run WebScraper.py to generate HTML pickle file

# Read HTML from pickle file
with open("temp\html_list", "rb") as fp:
    chapter_htmls = pickle.load(fp)

chapter_titles = []
chapter_text = []

# Extract Chapter Names from HTML
chap_title_html = BeautifulSoup(chapter_htmls[0], 'html.parser')
chap_title_page = chap_title_html.find(id="dropdown1")
for chapter_item in chap_title_page.find_all('a'):
    chapter_titles.append(chapter_item.get_text())
    #print(chapter_item.get_text())

