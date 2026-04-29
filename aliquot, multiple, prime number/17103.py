# 골드바흐 파티션
import sys
input = sys.stdin.readline
n = int(input())
lst = [False, False] + [True]*(1000001)
prime = []
for i in range(2, 1000001):
    if lst[i]:
        prime.append(i)
        for j in range(2*i, 1000001, i):
            lst[j] = False
for _ in range(n):
    ans = int(input())
    cnt = 0
    for p in prime:
        if p >= ans:
            break
        if not lst[ans - p] and p <= ans - p:
            cnt += 1
    print(cnt)

print(prime[:10])