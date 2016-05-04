# cython: boundscheck=False, wraparound=False, nonecheck=False
import numpy as np
cimport numpy as np
cimport cython


def convolve2(np.ndarray[np.double_t,ndim=2] A,
              np.ndarray[np.double_t,ndim=2] B):
    cdef np.ndarray[np.double_t,ndim=2] C = A.copy()
    cdef unsigned int n, m
    # 99% procent kompatybilnosci:
    # n,m = A.shape nie dziala
    n = A.shape[0]
    m = A.shape[1]
    cdef unsigned int k = B.shape[0]//2
    cdef unsigned int i, j, ai, aj
    for i in range(k, n-k):
        for j in range(k, m-k):
            C[i,j] = 0
            for ai in range(0, 2*k+1):
                for aj in range(0, 2*k+1):
                    C[i,j] += A[i+ai-k,j+aj-k]*B[ai,aj]
    return C

def sum3(np.ndarray[np.double_t] x):
    cdef np.double_t s = 0
    cdef unsigned int i, n = len(x)
    for i in range(0, n):
            s += x[i]
    return s

def pi4(unsigned int n):
    cdef double s = 1
    cdef double a = 1
    cdef unsigned int i
    for i in range(1, n+1):
            a = -a
            s += a/(2*i+1)
    return 4*s
