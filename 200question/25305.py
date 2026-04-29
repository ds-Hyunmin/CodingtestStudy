# n, k = map(int, input().split())
# lst = list(map(int, input().split()))
# for i in range(1, n):
#     for j in range(i, 0, -1):
#         if lst[j] > lst[j-1]:
#             lst[j], lst[j-1] = lst[j-1], lst[j]
# lst = lst[:k]
# print(lst[-1])

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

