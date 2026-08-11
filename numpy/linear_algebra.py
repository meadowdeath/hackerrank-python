import numpy

def get_determinant(matrix):
    return numpy.linalg.det(numpy.array(matrix, dtype=float))

if __name__ == '__main__':

    N = int(input().strip())
    matrix = [input().strip().split() for _ in range(N)]

    det_value = get_determinant(matrix)

    print(numpy.round(det_value, 2))