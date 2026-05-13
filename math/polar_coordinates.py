# Enter your code here. Read input from STDIN. Print output to STDOUT
from cmath import phase as c_phase

if __name__ == '__main__':
    z = complex(input())

    r = abs(z)
    phi = c_phase(z)

    print(r)
    print(phi)
