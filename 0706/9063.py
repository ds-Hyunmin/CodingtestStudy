# 대지

n = int(input())
# lst_x = []
# lst_y = []
# for i in range(n):
#     a, b = map(int, input().split())
#     lst_x.append(a)
#     lst_y.append(b)
# print((max(lst_x)-min(lst_x))*(max(lst_y)-min(lst_y)))
n = int(input())
lst = [[], []]
for i in range(n):
    a, b = map(int, input().split())
    lst[0].append(a)
    lst[1].append(b)
x = max(lst[0]) - min(lst[0])
y = max(lst[1]) - min(lst[1])
print(x*y)