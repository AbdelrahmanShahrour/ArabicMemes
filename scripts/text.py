import re
import string
import pyarabic
import pyarabic.araby as araby
from pyarabic.araby import tokenize, is_arabicrange, strip_tashkeel, strip_tatweel
from pyarabic.number import ArNumbers 

import easyocr
import pandas as pd
from tqdm.auto import tqdm

def normalize_text(text):
    text = text.strip()
    
    # remove twitter usernames, web addresses
    text = re.sub(r"#[\w\d]*|@[.]?[\w\d]*[\'\w*]*|https?:\/\/\S+\b|"r"www\.(\w+\.)+\S*|", '', text)

    # remove nonarabic words
    text = ' '.join(tokenize(text, conditions=is_arabicrange))

    # remove extra spaces
    text = re.sub(' +', ' ', text)

    return text

def extract_text(df):
	text = []
	for img in tqdm(df.file_name):
	  try:
	    text.append(reader.readtext(f'/content/Memes (final)/{img}', detail=0, paragraph=True)[0])
	  except FileNotFoundError:
	    print(f'File {img} not found')
	    continue
	  except IndexError:
	    print(f'File {img} has no text')

	print(len(text))

	df['text'] = text

	return df