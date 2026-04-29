import sys
input = sys.stdin.readline
n, m = map(int, input().split())
lst = [0]*(n+1)
for i in range(m):
    a, b, c = map(int, input().split())
    for j in range(a, b+1):
        lst[j] = c
for l in lst[1:]:
    print(l, end=' ')