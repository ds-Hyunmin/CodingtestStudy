import sys
input = sys.stdin.readline
n, m = map(int, input().split())
nset, mset = set(), set()
for _ in range(n):
    nset.add(input().rstrip())
for _ in range(m):
    mset.add(input().rstrip())
ans = sorted(nset&mset)
print(len(ans))
for a in ans:
    print(a)