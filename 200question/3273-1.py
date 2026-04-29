import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
ans = int(input())

arr.sort()
left, right = 0, n - 1
cnt = 0
while left < right:
    x = arr[left] + arr[right]
    if x == ans:
        cnt += 1
        left += 1
        right -= 1
    elif x < ans:
        left += 1
    else:
        right -= 1

print(cnt)
