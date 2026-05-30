# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

if __name__ == '__main__':
    n = int(input())
    letter_list = input.split()
    k = int(input())
    comb_letters = list(combinations(letter_list, k))
    count = 0

    for comb in  comb_letters:
        if 'a' in comb:
            count += 1

    a_probability = count / len(comb_letters)

    print(f"{a_probability:.3f}")