from collections import deque
import sys

input = sys.stdin.readline
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [0 for _ in range(n+1)]
visited = [False for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

arr = deque([])
def bfs(node):
    arr.append(node)
    visited[node] = True
    while arr:
        a = arr.popleft()
        for i in graph[a]:
            if not visited[i]:
                visited[i] = True
                distance[i] = distance[a] + 1
                arr.append(i)

bfs(x)

score = False
for i in range(len(distance)):
    if distance[i] == k:
        score = True
        print(i)

if not score:
    print(-1)