from LocalitySensitiveHashing import LocalitySensitiveHashing
import numpy as np
from Random_Projection import Random_Projection
import csv
# Use random projections to reduce dimensions
# load input data for random projections 
input_file = "data_for_random_projections.txt"
A=np.loadtxt(input_file)
n = A.shape[0]
dim = A.shape[1]
mode = 1
rand_obj = Random_Projection(mode, 0.1, n, dim)
# generate random projection matrix and reduce dimensions
B = rand_obj.get_reduced_input(A)
B = np.around(B, decimals = 3)
# write to csv file for performing lsh
with open('data_for_lsh.csv', 'w', newline='') as csvfile:
	docwriter = csv.writer(csvfile, delimiter=',')
	for doc in np.arange(n):
		docwriter.writerow(["document_" + str(doc+1)] + list(B[doc,:]))
d = B.shape[1]
lsh = LocalitySensitiveHashing( 
                   datafile = "data_for_lsh.csv",
                   dim = d,
                   r = 10,         
                   b = 14,          
              )
lsh.get_data_from_csv()
lsh.initialize_hash_store()
lsh.hash_all_data()
similarity_neighborhoods = lsh.lsh_basic_for_nearest_neighbors()
