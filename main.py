import numpy as np
from Random_Projection import Random_Projection
mode = 1
input_file = "data_for_random_projections.txt"
A=np.loadtxt(input_file)
print(A.shape)
n = A.shape[0]
dim = A.shape[1]
rand_obj = Random_Projection(mode, 0.1, n, dim)
print(rand_obj.k)

B =rand_obj.get_reduced_input(A)

print('\n')
print(B.shape)



