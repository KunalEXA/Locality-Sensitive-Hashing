from LocalitySensitiveHashing import LocalitySensitiveHashing
lsh = LocalitySensitiveHashing( 
                   datafile = "data_for_lsh.csv",
                   dim = 10,
                   r = 50,         
                   b = 100,          
              )
lsh.get_data_from_csv()
lsh.initialize_hash_store()
lsh.hash_all_data()
similarity_neighborhoods = lsh.lsh_basic_for_nearest_neighbors()