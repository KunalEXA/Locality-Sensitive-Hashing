# Near neighbor search using random  projections and LSH

This project uses reuters dataset to find similar documents using random projections and LSH. Random projections are used for reducing dimensionality and LSH is used for smart search.

### Prerequisites

Code is written in Python. Before you begin make sure you have the following dependencies installed.

```
csv
numpy
LocalitySensitiveHashing
scipy
BitVector

```

### Installing

Just download the code from the following github link.
To install Locality sensitive hashing library unzip the tar file (provided) and run the following command from within the locality sensitive package library
```
python setup.py install
```


## Running the project
Run lsh.py using the following command
```
python lsh.py

``` 

Wait for the prompt asking for document number. 
```
Enter the symbolic name for a data sample (must match names used in your datafile):
```
The documents are named 'document_1'. We have 100 such documents.

The program provides a set of near neighbors if any.

One can then manually go ahead and check the documents.

The default configuration that comes with the package makes use of only 100 documents. You can change this by going in the parsing.py file and changing the size of the matrix
by specifying the file pattern eg - "reut2-00". 
Then first run the parsing.py file and then run lsh.py

## Built With

* Python
* LocalitySensitiveHashing


## Authors

* **Ravi Nagarjun Akella** - *Initial work*
* **Kunal Bajaj** - *Initial work*
