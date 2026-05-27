# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby

if __name__ == '__main__':
    S = input()
    for key, group in groupby(S):
        group_size = len(list(group))

        print(f"({group_size}, {key})", end=' ')
