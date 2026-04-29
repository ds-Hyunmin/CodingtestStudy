import sys
input = sys.stdin.readline
n = int(input())
sch = []
for _ in range(n):
    sch.append(list(map(int, input().split())))
sch.sort(key = lambda x:(x[1], x[0]))
cnt, np = 0, -1
for start, end in sch:
    if np <= start:
        np = end
        cnt += 1
print(cnt)