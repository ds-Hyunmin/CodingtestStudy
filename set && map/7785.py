#회사에 있는 사람
import sys
input = sys.stdin.readline
n, dic = int(input()), {}
for i in range(n):
    a, b = map(str, input().split())
    if b == 'enter':dic[a] = 1
    else:del dic[a]
print("\n".join(sorted(list(dic.keys()), reverse=True)))