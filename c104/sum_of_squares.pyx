def sum_of_squares(int n):
    cdef int i
    cdef int result = 0
    for i in range(1, n + 1):
        result += i * i
    return result