# def qsort(arr):
#     if len(arr) < 2:
#         return arr
#     pivot = arr[0]
#     low, high = [], []
#
#     for value in arr[1:]:
#         if value < pivot:
#             low.append(value)
#         else:
#             high.append(value)
#     return qsort(low) + [pivot] + qsort(high)
# n, m = map(int, input().split())
# kst = list(map(int, input().split()))
# jst = list(map(int, input().split()))
# lst = kst + jst
# lst = qsort(lst)
# for l in lst:
#     print(l, end = ' ')

def counting_sort(arr):
    max_val = max(arr)
    count = [0]*(max_val+1)

    for num in arr:
        count[num] += 1
    idx = 0
    for i in range(len(count)):
        while count[i] > 0:
            arr[idx] = i
            idx += 1
            count[i] -= 1
    return arr

n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst += list(map(int, input().split()))
counting_sort(lst)
for l in lst:
    print(l, end = ' ')
