# k-Shingles
def kShingles(doc, k):
	return [doc[i:i+k] for i in range(len(doc) - k + 1)]

# word shingles
def wordShingles(doc, k):
	from nltk.corpus import stopwords
	import binascii
	# Split the document in space delimited words 
	words = [x.lower() for x in doc.split(" ")]
	word_shingles = set()
	for i in range(len(words) - k + 1):
		if words[i] in stopwords.words('english'):
			# Construct the shingle
			shingle = " ".join(words[i:i+k])
			shingle = shingle.encode("ascii")
			# Hash shingle using CRC32 and add it to the shingles set
			crc = binascii.crc32(shingle) & 0xffffffff
			word_shingles.add(crc)
	return word_shingles
	
# Jaccard Similarity
def jaccardSimilarity(list1, list2):
	intersection_len = len(set(list1).intersection(set(list2)))
	union_len = len(set(list1).union(set(list2)))
	return float(intersection_len)/union_len

