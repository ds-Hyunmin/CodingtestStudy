lst = []
for _ in range(5):
    lst.append(int(input()))
for i in range(1, len(lst)):
    for j in range(i, 0, -1):
        if lst[j] < lst[j-1]:
            lst[j], lst[j-1] = lst[j-1], lst[j]
print(sum(lst)//5)
print(lst[2])