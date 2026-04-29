import sys
input = sys.stdin.readline
n = int(input())
nset = set(map(int, input().split()))
m = int(input())
mset = list(map(int, input().split()))

for i in mset:
    if i in nset:
        print(1)
    else:print(0)