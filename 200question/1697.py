from collections import deque
n, k = map(int, input().split())
arr = [0]*100001

def bfs(i):
    queue = deque()
    queue.append(n)
    arr[i] = 1
    while queue:
        i = queue.popleft()
        for ni in (i-1, i+1, i*2):
            if 0 <= ni <= 100000 and arr[ni] == 0:
                queue.append(ni)
                arr[ni] = arr[i] + 1
    return arr[k]-1
print(bfs(n))