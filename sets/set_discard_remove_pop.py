if __name__ == '__main__':
    n = int(input())
    elements = set(map(int, input().split()))
    N = int(input())
    
    for i in range(N):
        action = input().split()
        if action[0] == 'pop':
            try:
                elements.pop()
            except KeyError:
                pass
        elif action[0] == 'remove':
            try:
                elements.remove(int(action[1]))
            except KeyError:
                pass
        elif action[0] == 'discard':
            elements.discard(int(action[1]))
    print(sum(elements))