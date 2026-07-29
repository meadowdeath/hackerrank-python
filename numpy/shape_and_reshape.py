import numpy

def shape_and_reshape(arr):
    # complete this function
    # use numpy.reshape
    return numpy.reshape(numpy.array(arr, int), (3, 3))

if __name__ == '__main__':

    arr = input().strip().split(' ')
    result = shape_and_reshape(arr)
    print(result)