import sys
input = sys.stdin.readline
n, m = map(int, input().split())
a_lst, b_lst = [], []
for i in range(n*2):
    if i < n:a_lst.append(list(map(int, input().split())))
    else:b_lst.append(list(map(int, input().split())))
for i in range(n):
    print(*[x+y for x, y in zip(a_lst[i], b_lst[i])], sep=' ')
