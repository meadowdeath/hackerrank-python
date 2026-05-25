# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement

if __name__ == '__main__':
    S, k = input().split()

    ordered_string = sorted(S)

    all_combination_with_replacement = combinations_with_replacement(ordered_string, int(k))

    for permutation in all_combination_with_replacement:
        print("".join(permutation))