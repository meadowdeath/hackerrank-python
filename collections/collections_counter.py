# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

if __name__ == '__main__':
    X = int(input())
    N = list(map(int, input().split()))
    customers_quantity = int(input())
    stock = Counter(N)
    total_price = 0
    
    for _ in range(customers_quantity):
        shoe_size, price = map(int, input().split())
        if stock[shoe_size] > 0:
            total_price += price
            stock[shoe_size] -= 1

    print(total_price)