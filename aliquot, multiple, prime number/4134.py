# 다음 소수
import sys
input = sys.stdin.readline
n = int(input())
def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

for _ in range(n):
    m = int(input())
    while True:
        if m == 0 or m == 1:
            print(2)
            break
        if isPrime(m):
            print(m)
            break
        else:
            m += 1


