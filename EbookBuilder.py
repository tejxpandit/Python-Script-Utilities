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

# Create Ebook
book = epub.EpubBook()

book.set_identifier('xxxxxx')
book.set_title('Book Title')
book.set_language('en')
book.add_author('Author Name')
book.add_metadata('DC', 'description', "The description of the story and what happens in the book to all the characters.")

book.set_cover("image.jpg", open('temp\cover.jpg', 'rb').read())

spine = ["cover", "nav"]
toc = ()

# Assemble Chapters
for c in range(chapters):
    title = chapter_titles[c]
    text = chapter_text[c]
    
    chap = epub.EpubHtml(title=title, 
                         file_name=("chap" + str(c) + ".xhtml"),
                         lang='en')
    
    
    paragraphs = text.split("\n\n")
    #print(paragraphs)
    
    html = "<h1>" + title + "</h1>"
    for para in paragraphs:
        html += "<p>" + para + "</p>"

    chap.set_content(html)
    book.add_item(chap)
    spine.append(chap)
    toc += (epub.Link("chap" + str(c) + ".xhtml", title, "chap" + str(c)),)

book.toc = toc
book.add_item(epub.EpubNcx())
book.add_item(epub.EpubNav())
book.spine = spine

epub.write_epub('My Ebook.epub', book, {})

print("Ebook created successfully!")