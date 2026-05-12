# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        setA_size = int(input())
        setA = set(map(int, input().split()))
        setB_size = int(input())
        setB = set(map(int, input().split()))

        print(setA.issubset(setB))
