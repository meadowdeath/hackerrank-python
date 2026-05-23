# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

if __name__ == '__main__':
    S, k = input().split()

    ordered_string = sorted(S)

    for size in range(1, int(k) + 1):
        
        current_combinatation = combinations(ordered_string, size)

        for combination in current_combinatation:
            print("".join(combination))