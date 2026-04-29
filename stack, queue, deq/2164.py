# 카드 2
from collections import deque
lst = deque(i for i in range(1, int(input())+1))

while len(lst) != 1:
    lst.popleft()
    lst.append(lst.popleft())
print(lst[0])