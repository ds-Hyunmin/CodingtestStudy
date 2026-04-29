def fib(n):
    if n == 1: return 1
    if n == 2: return 2
    if n == 3: return 4

    return fib(n-1)+fib(n-2)+fib(n-3)
t = int(input())
for _ in range(t):
    print(fib(int(input())))