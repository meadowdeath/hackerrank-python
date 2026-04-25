import string

def print_rangoli(size):
    # your code goes here
    length = (size * 2) - 1
    width = (size * 4) - 3
    center = length // 2
    alphabet_inv = list(string.ascii_lowercase)[:size][::-1]

    for row in range(length):
        distance = abs(row - center)
        quantity = size - distance
        alphabet_row = alphabet_inv[:quantity]
        full_alphabet_row = alphabet_row + alphabet_row[:-1][::-1]
        print(f"{"-".join(full_alphabet_row).center(width, '-')}")

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)