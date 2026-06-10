from collections import deque

actions = int(input())
queue = deque()
for _ in range(actions):
    action = input().split()
    if action[0] == 'append':
        queue.append(action[1])
    elif action[0] == 'appendleft':
        queue.appendleft(action[1])
    elif action[0] == 'pop':
        queue.pop()
    elif action[0] == 'popleft':
        queue.popleft()

print(*queue)