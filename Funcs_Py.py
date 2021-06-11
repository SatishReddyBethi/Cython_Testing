import numpy as np

def ArrayTesting(array_1):
    b = 0
    for i in range(0,array_1.shape[0]):
        b+=array_1[i]        
    return b

def MultiArray(multi_array):
    b=0
    for i in range(0,multi_array.shape[0]):
        b+=multi_array['obj_id'][i]
    return b