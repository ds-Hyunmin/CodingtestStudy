# 소수 구하기
m, n = map(int, input().split())
def isprime(num):
    if num < 2:
        return False
    for i in range(2, int(num**(1/2))+1):
        if num % i == 0:
            return False
    return True
for i in range(m, n+1):
    if isprime(i):
        print(i)