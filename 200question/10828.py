import sys
input = sys.stdin.readline
stack = []
for i in range(int(input())):
    enter = input()
    if 'push' in enter:
        a, b = enter.split()
        stack.append(int(b))
    elif enter == 'pop':
        if len(stack) > 0:
            print(stack[-1])
            stack.pop(-1)
        else:print(-1)
    elif enter == 'size':print(len(stack))
    elif enter == 'empty':
        if len(stack) > 0:print(0)
        else:print(1)
    elif enter == 'top':
        if len(stack) > 0:print(stack[-1])
        else:print(-1)