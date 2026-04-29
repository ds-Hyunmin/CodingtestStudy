import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
m = int(input())
graph = dict()
for _ in range(m):
    a, b = map(int, input().split())
    if a in graph.keys():
        graph[a].append(b)
    else:
        graph[a] = [b]
    if b in graph.keys():
        graph[b].append(a)
    else:
        graph[b] = [a]
def bfs(graph, start_node):
    queue = deque([start_node])
    visited = []
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            queue.extend(graph[node])
    return visited
print(len(bfs(graph, 1))-1)