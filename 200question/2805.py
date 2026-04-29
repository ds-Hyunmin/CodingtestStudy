import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = list(map(int, input().split()))
idx = 0
for i in range(1, max(lst)+1):
    new_lst = sum(x - i for x in lst if x-i > 0)
    if new_lst >= m:
        idx = i
    else:break
print(idx)