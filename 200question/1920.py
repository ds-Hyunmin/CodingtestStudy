import sys
input = sys.stdin.readline
n = int(input())
n_lst = list(map(int, input().split()))
m = int(input())
m_lst = list(map(int, input().split()))
for m in m_lst:
    if m in n_lst:print(1)
    else:print(0)