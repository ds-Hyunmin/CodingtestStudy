# 큐 2
import sys
from collections import deque
input = sys.stdin.readline
queue = deque()
for _ in range(int(input())):
    order = input().split()
    if order[0] == 'push':
        queue.append(order[1])
    elif order[0] == 'size':
        print(len(queue))
    elif order[0] == 'empty':
        if queue:print(0)
        else: print(1)
    elif queue:
        if order[0] == 'pop':print(queue.popleft())
        elif order[0] == 'front':print(queue[0])
        else:print(queue[-1])
    else:
        print(-1)