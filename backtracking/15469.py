# N과 M (1)
import sys
import itertools
n, m = map(int, sys.stdin.readline().split())
lst = [i for i in range(1, n+1)]
ans_lst = itertools.permutations(lst, m)
for i in ans_lst:
    for j in i:
        print(j, end=' ')
    print()