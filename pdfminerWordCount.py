# Title : PDF Miner Word Counter
# Author : Tej Pandit
# Date : April 2024

from nltk.tokenize import RegexpTokenizer
from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer

tokenizer = RegexpTokenizer(r'\w+')
words = []

# Extract Tokens from PDF
for page_layout in extract_pages("Nature_Neuromorphic_Computing_at_Scale__Final_.pdf"):
    for element in page_layout:
        if isinstance(element, LTTextContainer):
            # print(element.get_text())
            tokens = tokenizer.tokenize(element.get_text())
            words.extend(tokens)

