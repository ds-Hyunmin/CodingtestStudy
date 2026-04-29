n = int(input())
n_list = list(map(int, input().split()))
ans = 1
for i in range(1, n):
    if n_list[i - 1] >= n_list[i]:
        ans = 0
        print(ans)
        exit()
print(ans)