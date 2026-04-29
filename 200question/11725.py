import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n = int(input())
arr = [[]for _ in range(n+1)]

for _ in range(n-1):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)

ans = [0]*(n+1)
def dfs(node):
    for a in arr[node]:
        if ans[a] == 0:
            ans[a] = node
            dfs(a)
dfs(1)
for i in range(2, len(ans)):
    print(ans[i])