from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().strip())))

def bfs(x, y):
    queue = deque()
    queue.append([x, y])
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] ==1:
                queue.append([nx, ny])
                arr[nx][ny] = arr[x][y] + 1
    return arr[n-1][m-1]
print(bfs(0, 0))