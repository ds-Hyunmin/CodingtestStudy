answer = [1, 1, 2, 2, 2, 8]
lst = list(map(int, input().split()))
for i in range(6):
    lst[i] = answer[i]-lst[i]
print(*lst, sep=' ')