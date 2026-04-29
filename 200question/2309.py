# lst, lst_sum = [], 0
# a, b = 0, 0
# for _ in range(9):
#     a = int(input())
#     lst.append(a)
#     lst_sum += a
#
# for i in range(len(lst)):
#     for j in range(i, 0, -1):
#         if lst[j] < lst[j-1]:
#             lst[j], lst[j-1] = lst[j-1], lst[j]
#
# for i in range(len(lst)):
#     for j in range(i+1, len(lst)):
#         if lst[i] + lst[j] == lst_sum - 100:
#             lst[i], lst[j] = 0, 0
#
#             for l in lst:
#                 if l > 0:
#                     print(l)
#             exit()

lst, lst_sum = [], 0
a, b = 0, 0
for _ in range(9):
    a = int(input())
    lst.append(a)
    lst_sum += a

for i in range(len(lst)):
    for j in range(i, 0, -1):
        if lst[j] < lst[j-1]:
            lst[j], lst[j-1] = lst[j-1], lst[j]

for i in range(len(lst)):
    for j in range(i+1, len(lst)):
        if lst[i] + lst[j] == lst_sum - 100:
            a, b = i, j
lst.pop(b)
lst.pop(a)
for l in lst:
    print(l)