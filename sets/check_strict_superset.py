# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    setA = set(map(int, input().split()))
    N = int(input())
    super_set = []

    for _ in range(N):
        setN = set(map(int, input().split()))
        super_set.append(setA > setN)
        
    if False in super_set:
        print(False)
    else:
        print(True)