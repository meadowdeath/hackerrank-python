import numpy

def get_sum_axis_0(matrix):
    # complete this function
    # use numpy.sum
    return numpy.sum(numpy.array(matrix, int), axis=0)

def get_product(sum_axis_0):
    # complete this function
    # use numpy.prod
    return numpy.prod(sum_axis_0)

if __name__ == '__main__':

    n, m = map(int, input().strip().split(' '))
    matrix = [input().strip().split(' ') for _ in range(n)]

    sum_axis_0 = get_sum_axis_0(matrix)

    print(get_product(sum_axis_0))