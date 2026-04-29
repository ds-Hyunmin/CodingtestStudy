import sys
input = sys.stdin.readline
n, k = map(int, input().split())
cnt, lst = 0, []
for i in range(n):
    lst.append(int(input()))
lst.sort(reverse=True)
for i in range(n):
    a = k // lst[i]
    if a > 0:
        cnt += a
        k = k%lst[i]
print(cnt)