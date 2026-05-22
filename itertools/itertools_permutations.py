# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

if __name__ == '__main__':
    S, k = input().split()

    all_permutation = sorted(permutations(S, int(k)))

    for permutation in all_permutation:
        print("".join(permutation))