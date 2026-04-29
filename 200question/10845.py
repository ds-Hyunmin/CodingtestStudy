from collections import deque
queue = deque()
for _ in range(int(input())):
    ord = input().split()
    if ord[0] == 'push':
        queue.append(ord[1])
    if ord[0] == 'pop':
        if len(queue) != 0:
            print(queue.popleft())
        else:
            print(-1)
    if ord[0] == 'size':
        print(len(queue))
    if ord[0] == 'empty':
        if len(queue) > 0:
            print(0)
        else:print(1)
    if ord[0] == 'front':
        if len(queue) != 0:
            print(queue[0])
        else:
            print(-1)
    if ord[0] == 'back':
        if len(queue) != 0:
            print(queue[-1])
        else:
            print(-1)