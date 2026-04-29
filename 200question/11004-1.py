def counting_sort(arr):
    max_val = max(arr)
    count = [0] * (max_val+1)

    for num in arr:
        count[num] += 1
    idx = 0
    for i in range(len(count)):
        while count[i] > 0:
            arr[idx] = i
            idx += 1
            count[i] -= 1
    return arr

n, k = map(int, input().split())
lst = list(map(int, input().split()))
lst = counting_sort(lst)

print(lst[k-1])