# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

n, m  = list(map(int, input().split()))

final_dict = defaultdict(list)

for i in range(n):
    word = input()
    final_dict[word].append(i + 1)
    
for _ in range(m):
    word_b = input()
    
    if word_b in final_dict:
        print(' '.join(map(str, final_dict[word_b])))
    else:
        print(-1)