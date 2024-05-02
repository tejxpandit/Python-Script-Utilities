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

# Remove Numbers
filtered_words = []
for word in words:
    if not word.isdigit():  # Check if the word consists only of digits
        filtered_words.append(word)
words = filtered_words

# Special Section to remove everything before Abstract
start_idx = words.index('Abstract')
# print(words[start_idx-1])

# Special Section to remove everything after References
stop_idx = words.index('References')
# print(words[stop_idx+1])

# Offset (Internal Blocks)
offset_boxes = 1334 #1320

# Display Results
print(words[start_idx:stop_idx])
print(len(words[start_idx:stop_idx]))

word_count = (stop_idx - start_idx) - offset_boxes
print("The Word Count is " + str(word_count) + " words")

