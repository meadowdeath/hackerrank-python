# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

n = int(input())
supplies = OrderedDict()

for _ in range(n):
    item_name, net_price = input().rsplit(' ', 1)
    supplies[item_name] = int(net_price) + supplies.get(item_name, 0)
    
for item_name, net_price in supplies.items():
    print(f'{item_name} {net_price}')