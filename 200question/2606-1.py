n = int(input())
m = int(input())
arr = [[]for _ in range(n+1)]

for _ in range(m):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)

visited = [False] * (n+1)
def dfs(node):
    visited[node] = True
    for a in arr[node]:
        if not visited[a]:
            dfs(a)
dfs(1)
cnt = 0
for v in visited:
    if v == True:
        cnt += 1
print(cnt-1)
# adj = [[2, 1], [3, 0], [3, 0], [9, 8, 2, 1], [5], [7, 6, 4], [7, 5], [6, 5], [3], [3]]
# n = len(adj)
# visited = [False] * n
# def dfs(v):
#     visited[v] = True
#     print(v, ' ', end='')
#     for nxt in adj[v]:
#         if not visited[nxt]:
#             dfs(nxt)
# for i in range(n):
#     if not visited[i]:
#         dfs(i)
