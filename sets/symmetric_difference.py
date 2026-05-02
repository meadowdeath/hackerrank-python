# Enter your code here. Read input from STDIN. Print output to STDOUT
def symmetric_difference(set_a, set_b):
    symmetric_difference = set_a.symmetric_difference(set_b)

    for num in sorted(symmetric_difference):
        print(num)


if __name__ == '__main__':
    m = input().split()
    set_a = set(map(int, input().split()))
    n = input().split()
    set_b = set(map(int, input().split()))
    
    symmetric_difference(set_a, set_b)