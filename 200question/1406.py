import sys
input = sys.stdin.readline
word = input().strip()
left = [w for w in word]
right = []
for _ in range(int(input())):
    tx = list(input().split())
    if tx[0] == 'P':
        left.append(tx[1])
    if tx[0] == 'L':
        if left:
            right.append(left.pop())
    if tx[0] == 'D':
        if right:
            left.append(right.pop())
    if tx[0] == 'B':
        if left:
            left.pop()
result = ''.join(left+right[::-1])
print(result)