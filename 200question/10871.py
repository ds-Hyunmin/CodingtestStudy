# X보다 작은 수
n, x = map(int, input().split())
lst = list(map(int, input().split()))
for l in lst:
    if l < x: print(l, end=' ' )