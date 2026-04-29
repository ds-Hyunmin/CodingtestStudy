def bubble_sort(lst):
    cnt = 0
    for i in range(len(lst)-1, 0, -1):
        for j in range(i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                cnt += 1
    return cnt
for i in range(int(input())):
    arr = list(map(int, input().split()))
    num = arr.pop(0)
    print(num, bubble_sort(arr))