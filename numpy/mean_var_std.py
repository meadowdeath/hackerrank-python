import numpy

if __name__ == '__main__':
    
    n, m = map(int, input().strip().split(' '))
    matrix = numpy.array([input().strip().split(' ') for _ in range(n)], int)

    print(numpy.mean(matrix, axis=1))
    print(numpy.var(matrix, axis=0))
    print(round(numpy.std(matrix, axis=None), 11))