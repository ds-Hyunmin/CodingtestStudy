lst, ans = [], ''
for _ in range(5):
    lst.append(input())
for i in range(15):
    for j in range(5):
        try:
            if lst[j][i] != '':ans += lst[j][i]
        except:continue
print(ans)
