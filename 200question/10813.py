n, m = map(int, input().split())
lst = [i for i in range(n+1)]
tmp = 0
for _ in range(m):
    a, b = map(int, input().split())
    tmp = lst[a]
    lst[a] = lst[b]
    lst[b] = tmp
lst = lst[1:]
print(*lst, sep=' ')