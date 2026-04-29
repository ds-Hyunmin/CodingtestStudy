import sys
input = sys.stdin.readline
lst = []
for _ in range(int(input())):
    lst.append(int(input()))
cnt, mx = 1, lst[-1]
for i in range(len(lst)-2, -1, -1):
    if lst[i] > mx:
        cnt += 1
        mx = lst[i]
print(cnt)
