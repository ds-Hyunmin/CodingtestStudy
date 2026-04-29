import sys
input = sys.stdin.readline

def merge_sort(lst):
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2

    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])

    return merge(left, right)
def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

n, m = map(int, input().split())
n_lst, m_lst = set(), set()
for i in range(n+m):
    if i < n:
        n_lst.add(input().strip())
    else:
        m_lst.add(input().strip())

lst = merge_sort(list(sorted(n_lst & m_lst)))
print(len(lst))
for l in lst:
    print(l)