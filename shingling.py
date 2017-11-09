# k-Shingles
def kShingles(doc, k):
	return [doc[i:i+k] for i in range(len(doc) - k + 1)]

# word shingles
def wordShingles(doc, k):
	from nltk.corpus import stopwords
	words = doc.split()
	word_shingles = [words[i:i+k] for i in range(len(words) - k + 1) if words[i].lower() in stopwords.words('english')]
	return [" ".join(word_shingles[i]) for i in range(len(word_shingles))]
	
# Jaccard Similarity
def jaccardSimilarity(list1, list2):
	intersection_len = len(set(list1).intersection(set(list2)))
	union_len = len(set(list1).union(set(list2)))
	return float(intersection_len)/union_len

