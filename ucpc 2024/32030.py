# 두 배
import sys
from itertools import combinations
input = sys.stdin.readline
N = int(input())
S, C, T = input(), input(), input()
# D = {}
# for i in range(N):
#     D[S[i]]=C[i]
# print(D)
# for i in range(len(T), 0,-1):
#     for s, c in D.items():
#         if T[i] == c and T[i-1] == s:
#

x = len(T)

for i in range(1, (x // 2) + 1):  # 문자열 절반의 값을 for문으로 반복
    s = T[0:i]  # s변수에 i값을 증가시키며 대입
    count = int(x / i)  # count변수에 문자열이 length를 i의 값으로 나눈값을 대입

    # 전체 문자열이 s에 count를 곱한 값과 같다면 s에 반복되는 요소가 들어갔다는 의미이므로 break으로 반복문을 빠져나온다.
    if (s * count == T):
        print(s)
        break