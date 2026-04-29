n = 1
for _ in range(3):
    n *= int(input())
str_lst = [0 for _ in range(10)]
for i in str(n):
    str_lst[int(i)] += 1
for i in str_lst:
    print(i)