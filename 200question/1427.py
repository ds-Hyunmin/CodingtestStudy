num = input()
lst, ans = [], ''
for i in num:
    lst.append(int(i))
for i in range(1, len(lst)):
    for j in range(i, 0, -1):
        if lst[j] > lst[j-1]:
            lst[j], lst[j-1] = lst[j-1], lst[j]
for l in lst:
    ans += str(l)
print(ans)