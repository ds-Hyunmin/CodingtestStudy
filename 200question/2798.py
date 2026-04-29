n, m = map(int, input().split())
lst = list(map(int, input().split()))
mx = 0
for i in range(len(lst)):
    for j in range(i+1, n):
        for k in range(j+1, n):
            ans = lst[i]+lst[j]+lst[k]
            if ans > mx and ans <= m:
                mx = ans
print(mx)