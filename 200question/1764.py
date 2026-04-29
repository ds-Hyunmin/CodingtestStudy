n, m = map(int, input().split())
n_lst, m_lst = [], []
for i in range(n+m):
    if i < n:
        n_lst.append(input())
    else:
        m_lst.append(input())
for i in range(len(n_lst)):
    for j in range(i, 0, -1):
        if n_lst[j] < n_lst[j-1]:
            n_lst[j], n_lst[j-1] = n_lst[j-1], n_lst[j]
ans = []
for n in n_lst:
    if n in m_lst:
        ans.append(n)
print(len(ans))
for a in ans:
    print(a)