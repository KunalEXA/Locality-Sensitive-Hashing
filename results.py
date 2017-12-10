# Jaccard Similarity for selected documents
import shingling
import time
import numpy as np


"""
text_file = "final_pre_processed.txt"
text_file = open(text_file, "r")
docs = text_file.read().split('\n')

k = 3
shingles4 = shingling.kShingles(docs[3], k)
shingles15 = shingling.kShingles(docs[14], k)
shingles16 = shingling.kShingles(docs[15], k)
Jsim_4_15 = shingling.jaccardSimilarity(shingles4, shingles15)
Jsim_4_16 = shingling.jaccardSimilarity(shingles4, shingles16)
print([Jsim_4_15, Jsim_4_16])
# time comparision
start_time = time.time()
similarity_threshold = 0.20
docs = docs[0:500]
N = len(docs)
print(N)
similar_docs = []
k = 3
for i in np.arange(N):
	cur_similar = []
	shinglesi = shingling.kShingles(docs[i], k)
	for j in np.arange(i+1, N):
		shinglesj = shingling.kShingles(docs[j], k)
		if shingling.jaccardSimilarity(shinglesi, shinglesj) > similarity_threshold:
			cur_similar.append(j)
	similar_docs.append(cur_similar)
	
print (similar_docs[3], '\n', similar_docs[15])
print("--- %s seconds ---" % (time.time() - start_time))
"""
start_time = time.time()
input_file = "data_for_random_projections.txt"
A=np.loadtxt(input_file)
dim = A.shape[1]
start_time = time.time()
similarity_threshold = 0.20
A = A[0:500,:]
N =  A.shape[0]
print(N)
similar_docs = []
def cosine_dis(a, b):
	n1 = np.linalg.norm(a)
	n2 = np.linalg.norm(b)
	cos_theta = a.dot(b)/(n1*n2)
	return (cos_theta)
similarity_threshold = 0.7
for i in np.arange(N):
	cur_similar = []
	for j in np.arange(i+1, N):
		cur_similarity = cosine_dis(A[i,:], A[j,:])
		if cur_similarity > similarity_threshold:
			cur_similar.append(j)
	similar_docs.append(cur_similar)
	
print (similar_docs[3], '\n', similar_docs[15])
print("--- %s seconds ---" % (time.time() - start_time))