if __name__ == '__main__':
    N = int(input())
    my_list = []
    
    for _ in range(N):
        line = input().split(' ')
        action = line[0]
        args = [int(x) for x in line[1:]]
        if action == 'insert':
            my_list.insert(*args)
        elif action == 'print':
            print(my_list)
        elif action == 'remove':
            my_list.remove(args[0])
        elif action == 'append':
            my_list.append(args[0])
        elif action == 'sort':
            my_list.sort()
        elif action == 'pop':
            my_list.pop()
        elif action == 'reverse':
            my_list.reverse()       