# Enter your code here. Read input from STDIN. Print output to STDOUT
def calculate_happiness(elements, positive_set, negative_set):
    score = 0
    for num in elements:
        if num in positive_set:
            score += 1
        elif num in negative_set:
            score -= 1
    return score

if __name__ == '__main__':
    n, m = input().split()
    elements = list(map(int, input().split()))
    positive_set = set(map(int, input().split()))
    negative_set = set(map(int, input().split()))

    print(calculate_happiness(elements, positive_set, negative_set))