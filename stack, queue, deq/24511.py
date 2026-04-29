# queuestack
import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
M = int(input())
C = list(map(int, input().split()))

def queue(c, B, j, ans):
    ans2 = B[j]
    if ans == c:
        B[j] = c
    else:
        B[j] = ans
    return ans2

for i in range(M):
    ans, c = C[i], C[i]
    for j in range(N):
        if A[j] == 0:
            ans = queue(c, B, j, ans)

    print(ans, end=' ')


