n = int(input())
lst = list(map(int, input().split()))
mx = 0
for l in lst:
    if l > mx:mx = l
for i in range(len(lst)):
    lst[i]=lst[i]/mx*100
print(sum(lst)/n)