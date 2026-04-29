import sys
input = sys.stdin.readline
lst = [0]*10001
for i in range(int(input())):
    lst[int(input())] += 1
for l in range(len(lst)):
    if lst[l] != 0:
        for _ in range(lst[l]):
            print(l)