# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 13:24:17 2017

@author: Nagarjun
"""

from bs4 import BeautifulSoup
import os
from string import punctuation
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

word_dict = set()
final_pre_processed_str = ""
for _, value in preprocessed_input.items():
	value = value.lower()
	trans_table = value.maketrans('', '', punctuation)
	value = value.translate(trans_table)
	word_dict.update(value.split())
	final_pre_processed_str += value + '\n'
file = open("final_pre_processed.txt", 'w')
file.write(final_pre_processed_str)
file.close()


file = open("word_dictionary.txt", 'w')
for item in word_dict:
	file.write("%s\n" % item)
file.close()
<<<<<<< HEAD

word_index_dict = {k : v for v, k in enumerate(word_dict)}
N = len(word_dict)
count = 1
with open('input_final.csv', 'w', newline='') as csvfile:
	docwriter = csv.writer(csvfile, delimiter=',')
	for _, value in preprocessed_input.items():
		value = value.lower()
		trans_table = value.maketrans('', '', punctuation)
		value = value.translate(trans_table)
		word_list = value.split()
		doc_freq = [0]*N
		for word in word_list:
			index = word_index_dict[word]
			doc_freq[index] += 1
		count += 1
		docwriter.writerow(["document_" + str(count)] + doc_freq)
		if count == 100:
			break;
	
	
	
=======
    
>>>>>>> parent of 7683daf... input in CSV format
