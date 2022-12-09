import ctypes
import numpy
import os
import subprocess

HERE_DIR = os.path.dirname(__file__)



def get_platform():
    import platform
    import sys
    if sys.platform.startswith('linux'):
        system = 'linux'
        libenv = 'LD_LIBRARY_PATH'
    elif sys.platform.startswith('win'):
        system = 'windows'
        libenv = 'PATH'
    elif sys.platform.startswith('darwin'):
        system = 'osx'
        libenv = 'DYLD_LIBRARY_PATH'
    else:
        raise Exception("OS not supported yet.")

    if '64' in platform.architecture()[0]:
        plat = 'amd64'
    else:
        plat = 'x86'
    
    return system, libenv, plat
    
def build_library():
    import subprocess
    build_dir = os.path.join(HERE_DIR, 'build')
    os.makedirs(build_dir, exist_ok=True)
    cmd = f"cd {build_dir} && cmake .. && make && cd {HERE_DIR}"
    ret = subprocess.run(cmd, capture_output=True, shell=True)
    print(ret)

    return build_dir


class CMatMul:
    def __init__(self) -> None:
        system, libenv, plat = get_platform()
        build_dir = os.path.join(HERE_DIR, 'build')
        if system == 'osx':
            libpath = os.path.join(build_dir, 'libc_mat_mul.dylib')
        elif system == 'linux':
            libpath = os.path.join(build_dir, 'c_mat_mul.so')
        elif system == 'win':
            libpath = os.path.join(build_dir, 'c_mat_mul.dll') # not supported yet
        else:
            raise Exception("not supported OS.")
        if not os.path.isfile(libpath):
            build_dir = build_library()
        self.lib = ctypes.cdll.LoadLibrary(libpath)


        # the libriary
        # void mat_mul(
        #     const float * MatA, /* first matrix */
        #     const float * MatB, /* second matrix */
        #     float * ResMat,     /* resulting matrix */
        #     const int dim1,     /* first dimension of matrixA */
        #     const int dim2,     /* second dimension of matrixA */
        #     const int dim3      /* second dimension of matrixB */
        # )
        # self.lib.c_mat_mul.restype = ctypes.c_float
        self.lib.mat_mul.argtypes = [
            ctypes.POINTER(ctypes.c_float),
            ctypes.POINTER(ctypes.c_float),
            ctypes.POINTER(ctypes.c_float),
            ctypes.c_int,
            ctypes.c_int,
            ctypes.c_int,
        ]
    
    def matmul(self, matA, matB):
        dim11, dim12 = matA.shape
        dim21, dim22 = matB.shape
        if dim12 != dim21:
            raise ValueError(f"Expected matA.shape[1] == matB.shape[0], but got {dim12} and {dim21} .")
        
        matRes = numpy.zeros((dim11, dim22), dtype=numpy.float32)
        c_matA = matA.astype(numpy.float32).ctypes.data_as(ctypes.POINTER(ctypes.c_float))
        c_matB = matB.astype(numpy.float32).ctypes.data_as(ctypes.POINTER(ctypes.c_float))
        c_matRes = matRes.ctypes.data_as(ctypes.POINTER(ctypes.c_float))
        # calling the library
        self.lib.mat_mul(c_matA, c_matB, c_matRes, dim11, dim12, dim22)

        return matRes
