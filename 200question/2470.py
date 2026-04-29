n = int(input())
lst = list(map(int, input().split()))
lst.sort()

answer = 2000000000
start, end = 0, n-1

while start < end:
    ans = lst[start] + lst[end]
    if abs(ans) < answer:
        ans_i, ans_j = start, end
        answer = abs(ans)
    if ans < 0:
        start += 1
    else:
        end -= 1
print(lst[ans_i], lst[ans_j])