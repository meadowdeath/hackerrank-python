import numpy

if __name__ == '__main__':

    n, m = list(map(int, input().strip().split(' ')))

    # The code doesn't pass the test cases altough it works as it should 
    # The issue is the output format. The expected output is a matrix with 1's and 0's 
    # separated by spaces, while the output of numpy.eye() is a matrix with 1's and 0's without spaces.
    print(str(numpy.eye(n, m, dtype=float)).replace('1',' 1').replace('0',' 0'))
