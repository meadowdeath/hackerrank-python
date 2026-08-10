import numpy

if __name__ == '__main__':

    coefficients = list(map(float, input().strip().split()))
    x = float(input().strip())
    print(numpy.polyval(coefficients, x))