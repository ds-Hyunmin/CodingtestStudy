# 숫자 카드
import sys
n = int(sys.stdin.readline())
n_lst = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
m_lst = list(map(int, sys.stdin.readline().split()))
dic = {}
for n in n_lst:
    dic[n] = 0
for m in m_lst:
    if m not in dic:print(0, end=' ')
    else: print(1, end=' ')