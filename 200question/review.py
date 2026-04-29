import sys
input = sys.stdin.readline

arr = []
for _ in range(int(input())):
    arr.append(list(map(int, input().split())))

arr.sort(key = lambda x: (x[1], x[0]))

end = arr[0][1]
cnt = 1
for i in range(1, len(arr)):
    new_start = arr[i][0]
    if new_start >= end:
        cnt += 1
        end = arr[i][1]

print(cnt)