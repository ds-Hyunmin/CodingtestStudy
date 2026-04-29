# N과 M (2)
import sys
import itertools
n, m = map(int, sys.stdin.readline().split())
lst = [i for i in range(1, n+1)]
ans_lst = list(itertools.permutations(lst, m))
print(ans_lst)
for i in ans_lst:
    i = list(i)
    if i != sorted(i, reverse=False):
        print(f'sorted(i, reverse=False): {sorted(i, reverse=False)}')
        print(f'i: {i}')
        ans_lst.remove(tuple(i))
print(ans_lst)
# for i in ans_lst:
#     i = list(i)
#     for j in range(1, len(i)):
#         print(i)
#         if i[j] > i[j-1]:
#             print(i[j-1], end=' ')
#         if j == m-1:
#             print(i[j], end=' ')
#     print()