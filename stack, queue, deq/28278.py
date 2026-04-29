# 스택 2
import sys
input = sys.stdin.readline
stack = []
for _ in range(int(input())):
    n = input().split()
    m = n[0]
    if m == '1':
        stack.append(n[1])
    elif m == '2':
        if not stack:print(-1)
        else:print(stack.pop())
    elif m == '3':print(len(stack))
    elif m == '4':
        if not stack:print(1)
        else:print(0)
    elif m == '5':
        if not stack:print(-1)
        else:print(stack[-1])