n = int(input())
idx = 0
for i in range(1000000):
    ans, k = i, str(i)
    for j in range(len(k)):
        ans += int(k[j])
    if int(ans) == n:
        idx = i
        break
print(idx)