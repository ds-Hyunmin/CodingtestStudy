# def qsort(arr):
#     if len(arr)<2:
#         return arr
#     pivot = arr[0]
#     low, high = [], []
#     for value in arr[1:]:
#         if value < pivot:
#             low.append(value)
#         else:
#             high.append(value)
#     return qsort(low) + [pivot] + qsort(high)
# n, k = map(int, input().split())
# lst = list(map(int, input().split()))
# lst = qsort(lst)
# print(lst[1])

n, k = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
print(lst[k-1])