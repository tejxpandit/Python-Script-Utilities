import pickle
from ebooklib import epub

# IMP : First run WebScraper.py & HTMLparser.py to generate HTML pickle files

# Read Chapters from pickle file
with open("temp\chapter_titles", "rb") as fp:
    chapter_titles = pickle.load(fp)

with open("temp\chapter_text", "rb") as fp:
    chapter_text = pickle.load(fp)

# Verify Chapter Titles match Chapters
print("Titles : " + str(len(chapter_titles)))
print("Chapters : " + str(len(chapter_text)))
if len(chapter_titles) == len(chapter_text):
    print("Match")
    
else:
    print("Warning! Chapter Titles do not match Chapters")

chapters = len(chapter_text)

