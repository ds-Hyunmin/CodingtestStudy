# 구간 합 구하기 4
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
n_lst = list(map(int, input().split()))
lst, ans = [], 0
for n in n_lst:
    ans += n
    lst.append(ans)
for _ in range(m):
    a, b = map(int, input().split())
    if a == 1:
        print(lst[b-1])
    else:print(lst[b-1]-lst[a-2])