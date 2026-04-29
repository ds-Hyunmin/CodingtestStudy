num = int(input())
cnt = 5000
for n in range(1689):
    for m in range(1001):
        if 3*n + 5*m == num:
            if n+m < cnt:
                cnt = n + m
                break

if cnt == 5000:
    print(-1)
else:print(cnt)