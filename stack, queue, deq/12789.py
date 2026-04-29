# 도키도키 간식드리미
import sys
input = sys.stdin.readline
n = int(input())
lst = list(map(int, input().split()))
additional, ans = [], 1
while ans != n:
    if lst and lst[0] == ans:
        lst.pop(0)
        ans += 1
    elif additional and additional[-1] == ans:
        additional.pop(-1)
        ans += 1
    else:
        if len(additional) > 1 and additional[-1] > additional[-2]:
            print('Sad')
            sys.exit()
        additional.append(lst[0])
        lst.pop(0)

print('Nice')