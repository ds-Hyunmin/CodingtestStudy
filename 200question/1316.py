import sys
input = sys.stdin.readline
cnt = 0
for _ in range(int(input())):
    word = input()
    alpha = word[0]
    for i in range(1, len(word)):
        if alpha[-1] == word[i]:alpha += word[i]
        elif word[i] not in alpha:alpha += word[i]
    if alpha == word:cnt += 1
print(cnt)