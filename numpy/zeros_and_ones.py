import numpy

if __name__ == '__main__':
    dimensions = list(map(int, input().strip().split(' ')))

    print(numpy.zeros(dimensions, int))
    print(numpy.ones(dimensions, int))