n = int(input())
lst = []
for _ in range(n):
    lst.append(list(map(int, input().split())))
lst = sorted(lst, reverse=False)
for i in range(n):
    print(*lst[i], sep=' ')