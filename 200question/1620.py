import sys
input = sys.stdin.readline
n, m = map(int, input().split())
ndict = {}
mdict = {}
for i in range(1, n+1):
    ndict[i] = input().rstrip()
mdict = {v:k for k, v in ndict.items()}

for _ in range(m):
    a = input().rstrip()
    if a.isdigit():
        print(ndict[int(a)])
    else:
        print(mdict[a])