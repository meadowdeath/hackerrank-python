# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

if __name__ == '__main__':
    K, M = map(int, input().split())
    lists = []
    for _ in range(K):
        lists.append(list(map(int, input().split()))[1:])
               
    possible_sums = {sum(i**2 for i in x) % M for x in product(*lists)}
    
    print(max(possible_sums))