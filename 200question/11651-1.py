def qsort(arr):
    if len(arr) < 2:
        return arr
    pivot = arr[0]
    low, high = [], []
    for value in arr[1:]:
        if value[1] < pivot[1]:low.append(value)
        elif value[1] == pivot[1]:
            if value[0] < pivot[0]:low.append(value)
            else:high.append(value)
        else:high.append(value)
    return qsort(low) + [pivot] + qsort(high)
lst = []
for _ in range(int(input())):
    lst.append(list(map(int, input().split())))
lst = qsort(lst)
for l in lst:
    print(l[0], l[1])