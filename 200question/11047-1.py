import sys
input = sys.stdin.readline
n, k = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr.sort(reverse=True)
cnt = 0
for a in arr:
    p = k // a
    if p > 0:
        cnt += p
        k = k - (p*a)
print(cnt)