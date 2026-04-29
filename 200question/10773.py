import sys
input = sys.stdin.readline
sum = 0
lst = []
for _ in range(int(input())):
    a = int(input())
    if a != 0:
        sum += a
        lst.append(a)
    else:
        sum -= lst.pop()

print(sum)

