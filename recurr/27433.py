# 팩토리얼 2
def fac(n):
    if n <= 1: return 1
    else: return n * fac(n-1)
print(fac(int(input())))