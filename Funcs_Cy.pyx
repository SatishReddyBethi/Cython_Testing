import numpy as np

cdef packed struct Dtype:
    int obj_id
    float length
    float[2] pt1

cpdef ArrayTesting(int[:] array_1):
    cdef int b = 0
    cdef long i = 0
    for i in range(0,array_1.shape[0]):
        b+=array_1[i]        
    return int(b)

cpdef MultiArray(Dtype[:] multi_array):
    cdef long b = 0
    cdef long i = 0 
    for i in range(0,len(multi_array)):
        b+=multi_array[i].obj_id
    return b