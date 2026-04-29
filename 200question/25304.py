import sys
input = sys.stdin.readline
ans = int(input())
sum = 0
for i in range(int(input())):
    a, b = map(int, input().split())
    sum += a*b
if ans == sum:print('Yes')
else:print('No')