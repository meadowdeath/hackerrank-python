import numpy

def get_min_axis_1(matrix):
    # complete this function
    # use numpy.min
    return numpy.min(numpy.array(matrix, int), axis=1)

def get_max_value(min_axis_1):
    # complete this function
    # use numpy.max
    return numpy.max(min_axis_1)

if __name__ == '__main__':
    n, m = map(int, input().strip().split(' '))
    matrix = [input().strip().split(' ') for _ in range(n)]

    min_axis_1 = get_min_axis_1(matrix)

    print(get_max_value(min_axis_1))