import numpy

def concatenate(matrix1, matrix2, axis):
    # complete this function
    # use numpy.concatenate
    return numpy.concatenate((numpy.array(matrix1, int), numpy.array(matrix2, int)), axis=axis)

if __name__ == '__main__':
    n, m, p = map(int, input().strip().split(' '))
    matrix1 = [input().strip().split(' ') for _ in range(n)]
    matrix2 = [input().strip().split(' ') for _ in range(m)]

    print(concatenate(matrix1, matrix2, axis=0))