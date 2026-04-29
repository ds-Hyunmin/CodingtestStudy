import sys
from collections import deque
input = sys.stdin.readline
n, m, v = map(int, input().split())
visited = [False]*(n+1)
visited[v] = True
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, w = map(int, input().split())
    graph[u].append(w)
    graph[w].append(u)

for arr in graph:
    arr.sort()

def dfs(node):
    print(node, end=' ')
    for nxt in graph[node]:
        if not visited[nxt]:
            visited[nxt] = True
            dfs(nxt)

def bfs(node):
    arr = deque([node])
    print(node, end=' ')
    while arr:
        nxt = arr.popleft()
        for i in graph[nxt]:
            if not visited[i]:
                visited[i] = True
                print(i, end=' ')
                arr.append(i)

dfs(v)
print()
visited = [False]*(n+1)
visited[v] = True
bfs(v)