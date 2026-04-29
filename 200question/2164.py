from collections import deque
n = int(input())
lst = deque(i for i in range(1, n+1))
while lst[0]!=lst[-1]:
    lst.popleft()
    lst.append(lst.popleft())
lst = list(lst)
print(lst[0])