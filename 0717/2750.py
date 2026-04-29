import sys
input = sys.stdin.readline
n = int(input())
lst = []
for _ in range(n):
    lst.append(int(input()))
for _ in range(n):
    mn = min(lst)
    print(mn)
    lst.remove(mn)