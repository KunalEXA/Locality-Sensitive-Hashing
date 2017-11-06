# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 13:24:17 2017

@author: Nagarjun
"""
"""
from bs4 import BeautifulSoup
import os
input_directory = "dataset"
input_string = ""
preprocessed_input = {}
count = 0
for (_, _, filenames) in os.walk(input_directory):
    for filename in filenames:
        if filename.startswith("reut2-") and filename.endswith(".sgm"):
            text_file = open(input_directory + "/" + filename, "r")
            lines = text_file.readlines()
            for s in lines:
                input_string += s
            

soup = BeautifulSoup(input_string, "html.parser")
all_text = soup.find_all("body")
for text in all_text:
    text_str = (str(text))[6:]
    text_str = " ".join(text_str[:text_str.rfind("Reuter")].split())
    preprocessed_input[count] = text_str
    count += 1
"""

final_pre_processed_str = ""
for _, value in preprocessed_input.items():
    final_pre_processed_str += value + '\n'
    
file = open("final_pre_processed.txt", 'w')
file.write(final_pre_processed_str)
file.close()
    