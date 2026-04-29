import sys
input = sys.stdin.readline
def top():
    if len(lst) > 0:print(lst[-1])
    else: print(-1)
def size():
    print(len(lst))
def empty():
    if len(lst) == 0:print(1)
    else: print(0)
def pop():
    a = -1
    if len(lst) > 0:a = lst.pop()
    print(a)

n = int(input())
lst = []
for _ in range(n):
    m = input().strip()
    m = m.split()
    if m[0] == 'push':
        lst.append(m[1])
    if m[0] == 'top':
        top()
    if m[0] == 'empty':
        empty()
    if m[0] == 'size':
        size()
    if m[0] == 'pop':
        pop()