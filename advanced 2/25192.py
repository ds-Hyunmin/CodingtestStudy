# 인사성 밝은 곰곰이
import sys
input = sys.stdin.readline
total_cnt, cnt = 0, []
n = int(input())
for i in range(n):
    enter = input().strip('[]\n')
    if enter == 'ENTER':
        total_cnt += len(set(cnt))
        cnt = []
    else:
        cnt.append(enter)
    if i == n-1:
        total_cnt += len(set(cnt))
print(total_cnt)
