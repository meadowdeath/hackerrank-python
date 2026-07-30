import numpy

def transpose(arr):
    # complete this function
    # use numpy.transpose
    return numpy.transpose(numpy.array(arr, int))

def flatten(arr):
    # complete this function
    # use numpy.flatten
    return numpy.array(arr, int).flatten()
if __name__ == '__main__':
    
    n, m = map(int, input().strip().split(' '))
    matrix = [input().strip().split(' ') for _ in range(n)]

    print(transpose(matrix))
    print(flatten(matrix))