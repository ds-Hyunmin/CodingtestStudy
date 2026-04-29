import sys
input = sys.stdin.readline
N = int(input())
# node = [0 for _ in range(200000)]
node = {}
for _ in range(N):
    n, h = map(int, input().split())
    if h in node:
        node[h].append(n)
    else:
        node[h] = [n]
print(node)