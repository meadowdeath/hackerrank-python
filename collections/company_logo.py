from collections import Counter

if __name__ == '__main__':
    s = sorted(input())
    counter = Counter(s)

    for char, count in counter.most_common(3):
        print(f"{char} {count}")

