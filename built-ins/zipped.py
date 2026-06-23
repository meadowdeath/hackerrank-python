# Enter your code here. Read input from STDIN. Print output to STDOUT
n, x = map(int, input().split())
data = [list(map(float, input().split())) for _ in range(x)]
for row in zip(*data):
    print(f"{sum(row) / x:.1f}")