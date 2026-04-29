import sys
input = sys.stdin.readline
def dfs(x, y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if  0 <= nx < n and 0 <= ny < m:
            if arr[nx][ny]== 1:
                arr[nx][ny] = -1
                dfs(nx, ny)

for _ in range(int(input())):
    m, n, k = map(int, input().split())
    cnt = 0
    arr = [[0]*m for _ in range(n)]

    for _ in range(k):
        a, b = map(int, input().split())
        arr[b][a] = 1

    for i in range(n):
        for j in range(m):
            if arr[i][j] > 0:
                dfs(i, j)
                cnt += 1
    print(cnt)
