# 다리 놓기
import sys
input = sys.stdin.readline

def comb(arr, idx):
    used = [False for i in range(len(arr))]
    if len(arr) == n:
        print(arr, end=" ")
        return arr

    for i in range(idx + 1, len(array)):
        if used[i] == False:
            used[i] = True
            comb(i, arr + [array[i]])
            used[i] = False


for _ in range(int(input())):
    n, li = map(int, input().split())
    array = [i for i in range(1, li+1)]
    print(len(comb([], n)))