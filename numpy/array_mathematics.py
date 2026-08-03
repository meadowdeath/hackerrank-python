import numpy

class ArrayMathematics:
    def __init__(self, n, m):
        self.n = n
        self.m = m

    def add(self, A, B):
        return numpy.add(A, B)

    def subtract(self, A, B):
        return numpy.subtract(A, B)

    def multiply(self, A, B):
        return numpy.multiply(A, B)

    def divide(self, A, B):
        return numpy.floor_divide(A, B)

    def mod(self, A, B):
        return numpy.mod(A, B)

    def power(self, A, B):
        return numpy.power(A, B)

if __name__ == '__main__':
    n, m = list(map(int, input().strip().split(' ')))
    A = numpy.array([list(map(int, input().strip().split(' '))) for _ in range(n)])
    B = numpy.array([list(map(int, input().strip().split(' '))) for _ in range(n)])

    array_math = ArrayMathematics(n, m)

    print(array_math.add(A, B))
    print(array_math.subtract(A, B))
    print(array_math.multiply(A, B))
    print(array_math.divide(A, B))
    print(array_math.mod(A, B))
    print(array_math.power(A, B))