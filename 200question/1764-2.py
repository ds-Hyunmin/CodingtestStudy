n, m = map(int, input().split())
nset, mset = set(), set()
for _ in range(n):
    nset.add(input().strip())
for _ in range(m):
    mset.add(input().strip())

lst = list(sorted(nset&mset))

for i in range(1, len(lst)):
    for j in range(i, 0, -1):
        if lst[j] < lst[j-1]:
            lst[j], lst[j-1] = lst[j-1], lst[j]
print(len(lst))
for l in lst:
    print(l)