import time
import pandas as pd
import numpy as np

with open('subset_elemets.txt') as f:
        subset_elements = f.read().split('\n')
    
with open('all_elements.txt') as f:
    all_elements = f.read().split('\n')

def Number_elements(file1,file2):
    start = time.time()

    verified_element = np.intersect1d(np.array(file1), np.array(file2)) 

    print(len(verified_element))
    print(f'Duration: {time.time() - start} seconds')

Number_elements(subset_elements, all_elements)
