import sys
input = sys.stdin.readline
lst = []
for _ in range(int(input())):
    a, b = input().split()
    lst.append([int(a), b])
lst = sorted(lst, key = lambda x:x[0])
for i in range(len(lst)):
    print(*lst[i])
