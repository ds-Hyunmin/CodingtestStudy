import sys
input = sys.stdin.readline
stack = []
for _ in range(int(input())):
    tx = input().strip()
    if tx[0] == 'push':
        stack.append(tx[1])
    elif tx[0] == 'pop':
        if stack:print(stack.pop())
        else:print(-1)
    elif tx[0] == 'size':
        print(len(stack))
    elif tx[0] == 'empty':
        if stack:print(0)
        else:print(1)
    elif tx[0] == 'top':
        if stack:print(stack[-1])
        else: print(-1)