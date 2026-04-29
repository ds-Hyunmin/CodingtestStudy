n = int(input())
lst = list(map(int, input().split()))
lst.sort()
tmp, ans = 0, 0
for l in lst:
    ans += (tmp + l)
    tmp += l
print(ans)