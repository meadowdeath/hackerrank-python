if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    first = float('-inf')
    second = float('-inf')

    for num in arr:
        if num > first:
            second = first
            first = num
        elif second < num < first:
            second = num

    print(second)