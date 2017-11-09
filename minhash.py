import shingling
import random

max_int = 2**32 - 1
c = 4294967311

def pickHashCoeff(n):
	rand_int_list = []
	while n > 0:
		rand_int = random.randint(0, max_int)
		while rand_int in rand_int_list:
			rand_int = random.randint(0, max_int)
		rand_int_list.append(rand_int)
		n = n-1
	return rand_int_list

n = 10
A = pickHashCoeff(n)
B = pickHashCoeff(n)

signatures = []
no_of_docs = 10
# Dictionary to store shingle sets of all docs

docs_file = "final_pre_processed.txt"
f = open(docs_file, "rU")

for i in range(no_of_docs):
	doc = f.readline()
	cur_shingles_set = shingling.wordShingles(doc, 3)
	cur_signature = []
	for j in range(n):
		a = A[j]
		b = B[j]
		minhash_code = c + 1
		for cur_shingle in cur_shingles_set:
			hash_code = ((a * cur_shingle) + b) % c
			if hash_code < minhash_code:
				minhash_code = hash_code
		cur_signature.append(minhash_code)
	signatures.append(cur_signature)
f.close


