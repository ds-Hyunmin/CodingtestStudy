import sys
input = sys.stdin.readline

n = int(input())
nlst = list(map(int, input().split()))
m = int(input())
mlst = list(map(int, input().split()))

n_dict = {}
for n in nlst:
    if n in n_dict:
        n_dict[n] += 1
    else:
        n_dict[n] = 1
for m in mlst:
    if m in n_dict:
        print(n_dict[m], end=' ')
    else:
        print(0, end=' ')