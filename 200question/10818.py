# 최소, 최대
n = int(input())
lst = list(map(int, input().split()))
mn = 1000000
mx = -1000000
for l in lst:
    if l < mn:mn = l
    if l > mx:mx = l
print(mn, mx)