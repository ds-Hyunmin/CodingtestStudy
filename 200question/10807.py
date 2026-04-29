n = int(input())
lst = list(map(int, input().split()))
ans = int(input())
cnt = 0
for l in lst:
    if l == ans: cnt+=1
print(cnt)