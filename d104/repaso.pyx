
import numpy as np

cimport cython
cimport numpy as cnp

cnp.import_array()

ctypedef cnp.float64_t DTYPE_t

# @cython.boundscheck(False) # turn off bounds-checking for entire function
# @cython.wraparound(False)  # turn off negative index wrapping for entire function
# def diff_means(cnp.ndarray a, cnp.ndarray b):
#     a_mean = a.mean()
#     b_mean = b.mean()

#     return a_mean - b_mean

def diff_means(cnp.ndarray a, cnp.ndarray b):
    cdef double sum_a = 0.0
    cdef double sum_b = 0.0

    cdef double a_mean = 0.0
    cdef double b_mean = 0.0

    cdef int n_a = 0
    cdef int n_b = 0

    n_a = a.size
    n_b = b.size

    for ai in a:
        sum_a += ai

    for bi in b:
        sum_b += bi

    a_mean = sum_a / n_a
    b_mean = sum_b / n_b

    return a_mean - b_mean