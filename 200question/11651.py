n = int(input())
lst = []
for _ in range(n):
    lst.append(list(map(int, input().split())))

print(lst[0][1])
for i in range(len(lst)):
    for j in range(i, 0, -1):
        if lst[j][1] < lst[j-1][1]:
            lst[j], lst[j-1] = lst[j-1], lst[j]
        elif lst[j][1] == lst[j-1][1]:
            if lst[j][0] < lst[j-1][0]:
                lst[j], lst[j-1] = lst[j-1], lst[j]
