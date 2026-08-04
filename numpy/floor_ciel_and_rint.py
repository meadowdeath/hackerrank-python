import numpy

if __name__ == '__main__':

    # The code doesn't pass the test cases altough it works as it should.
    # The issue is the output format. The expected output use an extra space before positive numbers, 
    # while the output of numpy.floor(), numpy.ceil() and numpy.rint() doesn't have it.
    # We set the sign option to ' ' to add a space before positive numbers.
    numpy.set_printoptions(sign=' ')

    array = numpy.array(list(map(float, input().strip().split(' '))))

    print(numpy.floor(array))
    print(numpy.ceil(array))
    print(numpy.rint(array))