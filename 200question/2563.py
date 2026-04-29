n = int(input())
lst = [[0]*100 for _ in range(100)]
for _ in range(n):
    a, b = map(int, input().split())
    for i in range(a, a+10):
        for j in range(b, b+10):
            lst[i][j]=1
cnt = 0
for i in range(100):
    for j in range(100):
        if lst[i][j] == 1:cnt += 1
print(cnt)