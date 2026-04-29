# 통계학
import sys
input = sys.stdin.readline
n = int(input())
lst, max_cnt, lst_cnt = [], [], [0] * 8001
for _ in range(n):
    m = int(input())
    lst.append(m)
    lst_cnt[m+4000] += 1
mx = max(lst_cnt)
for i in range(len(lst_cnt)):
    if lst_cnt[i] == mx:
        max_cnt.append(i-4000)
max_cnt = sorted(max_cnt, reverse=False)
lst = sorted(lst, reverse=False)
print(round(sum(lst)/n))
print(lst[n//2])
if len(max_cnt) == 1:
    print(max_cnt[0])
else:
    print(max_cnt[1])
print(lst[-1]-lst[0])
