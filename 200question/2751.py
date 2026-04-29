import sys
input = sys.stdin.readline
lst = []
for i in range(int(input())):
    lst.append(int(input()))
lst.sort(reverse=False)
for l in lst:
    print(l)