import sys
input = sys.stdin.readline
fst = int(input())
fst_lst = list(map(int, input().split()))
lst = [0]*20000001
for f in fst_lst:
    lst[f] += 1
sec = int(input())
sec_lst = list(map(int, input().split()))
for s in sec_lst:
    print(lst[s], end=' ')