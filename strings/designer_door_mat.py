def manufacture(N, M):

    center = N // 2

    for row in range(N):
        distance = abs(row - center)
        if row == center:
            print(f"{'WELCOME'.center(M, '-')}")
        else:
            print(f"{('.|.' * ((center - distance) * 2 + 1)).center(M, '-')}")


if __name__ == '__main__':
    N, M = map(int, input().split())
    manufacture( N, M)

