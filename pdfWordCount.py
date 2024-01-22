# Title : PDF Word Counter
# Author : Tej Pandit
# Date : September, 2021

from io import StringIO
import nltk
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

