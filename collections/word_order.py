# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

n = int(input())
words_counts = OrderedDict()

for _ in range(n):
    word = input().strip()
    words_counts[word] = words_counts.get(word, 0) + 1
    
print(len(words_counts))
print(*words_counts.values())