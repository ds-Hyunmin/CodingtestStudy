from collections import deque
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    func = input().strip()
    n = int(input())
    s = input().strip()
    if s == '[]':
        arr = deque()
    else:
        arr = deque(map(int, s[1:-1].split(',')))
    m = 'f'
    error = False
    for f in func:
        if f == 'D':
            if not arr:
                error = True
                break
            elif m == 'f':
                arr.popleft()
            else:
                arr.pop()
        else:
            if m == 'f':
                m = 'b'
            else:
                m = 'f'
    if not error:
        arr = list(arr)
        if m == 'b':
            arr = arr[::-1]
        print('[' + ','.join(map(str, arr)) + ']')
    else:
        print('error')
