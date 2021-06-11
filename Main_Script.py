import Funcs_Py as py
import Funcs_Cy as cy
import time
import numpy as np

array_1 = np.ones((2_000_000), dtype = np.intc)
multi_array = np.ones(2_000_000,dtype=np.dtype([('obj_id',np.intc),('length',np.float32),('pt1',np.float32,2)]))

tic = time.perf_counter()
b = py.ArrayTesting(array_1)
toc = time.perf_counter()
print(f"[INFO] Python:{toc - tic:0.8f} seconds")

tic = time.perf_counter()
c = cy.ArrayTesting(array_1)
toc = time.perf_counter()
print(f"[INFO] Cython:{toc - tic:0.8f} seconds")

tic = time.perf_counter()
d = py.MultiArray(multi_array)
toc = time.perf_counter()
print(f"[INFO] Python:{toc - tic:0.8f} seconds")

tic = time.perf_counter()
e = cy.MultiArray(multi_array)
toc = time.perf_counter()
print(f"[INFO] Cython:{toc - tic:0.8f} seconds")