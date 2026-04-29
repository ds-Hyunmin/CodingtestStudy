n = int(input())
lst = list(map(int, input().split()))
x = int(input())

def qsort(arr):
    if len(arr)<2:
        return arr
    pivot = arr[0]
    low, high = [], []
    for value in arr[1:]:
        if value <pivot:
            low.append(value)
        else:
            high.append(value)
    return qsort(low) + [pivot] + qsort(high)


lst = qsort(lst)

cnt = 0
left, right = 0, n-1

while left<right:
    ans = lst[left] + lst[right]
    if ans == x:
        cnt += 1
        left += 1
        right -= 1
    elif ans < x:
        left += 1
    else:
        right -= 1
print(cnt)