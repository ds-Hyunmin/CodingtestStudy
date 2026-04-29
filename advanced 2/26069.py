# 붙임성 좋은 총총이
import sys
input = sys.stdin.readline
met = ['ChongChong']
for _ in range(int(input())):
    a, b = map(str, input().split())
    if a in met or b in met:
        met.append(a)
        met.append(b)
print(len(set(met)))

