# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    A = int(input())
    setA = set(map(int, input().split()))
    N = int(input())
    for _ in range(N):
        command, num = input().split()
        setN = set(map(int, input().split()))
        
        if command == 'intersection_update':
            setA.intersection_update(setN)
        elif command == 'update':
            setA.update(setN)
        elif command == 'symmetric_difference_update':
            setA.symmetric_difference_update(setN)
        elif command == 'difference_update':
            setA.difference_update(setN)
    
    print(sum(setA))