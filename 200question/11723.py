import sys
input = sys.stdin.readline
s = []
def calc(a, b):
    b = int(b)
    if a == 'add':
        if b not in s:s.append(b)
    elif a == 'remove':
        if b in s:s.remove(b)
    elif a == 'check':
        if b in s:print(1)
        else:print(0)
    else:
        if b in s:s.remove(b)
        else:s.append(b)

for _ in range(int(input())):
    order = input()
    if 'all' in order:
        s = [i for i in range(1, 21)]
    elif 'empty' in order:
        s = []
    elif order != 'all' and order != 'empty':
        a, b = order.split()
        calc(a, b)
