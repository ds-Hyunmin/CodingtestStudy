n = int(input())
lst = list(map(int, input().split()))
cnt = 0
for l in lst:
    if l != 1:
        i = 2
        while i != l:
            if l % i != 0:
                i += 1
            else:
                print(cnt)
                cnt += 1
                break
print(cnt)