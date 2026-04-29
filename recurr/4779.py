n = int(input())
ans = [1]*3**n
while [1, 1] not in ans:
    ans[int(n/3):int(2*n/3)] = [0]*round((n/3))