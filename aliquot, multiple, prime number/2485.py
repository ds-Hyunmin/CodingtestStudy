# 가로수
from functools import reduce
import sys, math
input = sys.stdin.readline
n = int(input())
lst, mini_lst = [], []
for i in range(n):
    lst.append(int(input()))
    if i > 0:
        ans = lst[i]-lst[i-1]
        mini_lst.append(ans)
temp = reduce(math.gcd, mini_lst)
cnt = 0
for i in range(1, n):
    if lst[i-1] + temp != lst[i]:
        cnt += (lst[i] - lst[i-1]) / temp - 1

print(int(cnt))


# 1
# 3
# 7
# 13
#
# 5, 9, 11