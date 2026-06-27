# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
elements = input().split()

print(all(int(x) >= 0 for x in elements) and any(x == x[::-1] for x in elements))