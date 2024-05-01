# Title : PDF Word Counter
# Author : Tej Pandit
# Date : September, 2021

from io import StringIO
# import nltk
# nltk.download('punkt') # --> for first time only
from nltk.tokenize import word_tokenize 

from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser

def containsNumber(value):
    for character in value:
        if character.isdigit():
            return True
    return False
    
output_string = StringIO()
with open('Nature_Bio.pdf', 'rb') as in_file:
    parser = PDFParser(in_file)
    doc = PDFDocument(parser)
    rsrcmgr = PDFResourceManager()
    device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    for page in PDFPage.create_pages(doc):
        interpreter.process_page(page)

text = output_string.getvalue()

tokens = word_tokenize(text) 

punctuations = ['.','(',')',';',':','[',']',','] 

keywords1 = [word for word in tokens if not word in punctuations] # remove punctuation
keywords = [word for word in keywords1 if not containsNumber(word)] # remove all numbers

# Special Section to ignore everything before Abstract
start_idx = keywords.index('Abstract')

# Special Section to ignore everything after References
stop_idx = keywords.index('References')

print(keywords)
print(len(keywords))
print(stop_idx - start_idx)

'''
import PyPDF2
import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize 

filename = 'Nature_Bio.pdf'  
pdfFileObj = open(filename,'rb') 

pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 

num_of_pages = pdfReader.numPages 
count = 0 
text = "" 

while count < num_of_pages: 
    pageObj = pdfReader.getPage(count) 
    count +=1 
    text += pageObj.extractText()
    print(pageObj)

tokens = word_tokenize(text) 

punctuations = ['.','(',')',';',':','[',']',','] 

keywords = [word for word in tokens if not word in punctuations] 

print(text)
'''