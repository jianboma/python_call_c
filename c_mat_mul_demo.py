import os, sys
import numpy as np

__dir__ = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.join(__dir__, '..'))

from c_mat_mul import *

cmatmul = CMatMul()

dim1, dim2, dim3 = 3, 4, 5
matA = np.zeros((dim1, dim2), dtype=np.float32) + 1.0
matB = np.zeros((dim2, dim3), dtype=np.float32) + 2.0

matRes = cmatmul.matmul(matA, matB)
print(matRes)

