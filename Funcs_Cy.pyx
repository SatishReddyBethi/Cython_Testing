import numpy as np
# cimport Util_Cy
# import Util_Cy as Util

cdef packed struct Dtype:
    int obj_id
    float length
    float[2] pt1

cpdef ArrayTesting(int[:] array_1):
    cdef int b = 0
    cdef long i = 0
    # Util.ExtraFunc()
    for i in range(0,array_1.shape[0]):
        b+=array_1[i]        
    return int(b)

cpdef MultiArray(Dtype[:] multi_array):
    cdef long b = 0
    cdef long i = 0 
    dtype_ = np.dtype([('obj_id',np.intc),('length',np.float32),('pt1',np.float32,2)])
    cdef Dtype[:] All_Obj = np.zeros((0,),dtype=dtype_)
    cdef Dtype obj = np.array((1,0.2,np.array([2,3],dtype=np.float32)),dtype=dtype_)
    All_Obj_ = np.hstack([obj,obj])
    cdef Dtype[:] _All_Obj = All_Obj_
    print(_All_Obj)
    for i in range(0,len(multi_array)):
        b+=multi_array[i].obj_id
    return b

cpdef float[:] ReturnTypes(int[:] b):
    print(b)
    cdef float[:] a = np.array([2,3,4],dtype=np.float32) 
    return a

def TestLoop():
    cdef int n = 2_000_000
    cdef long b = 0
    cdef long i = 0
    for i in range(n):
        b+=i
    return b