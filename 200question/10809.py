word = input()
alpha = 'abcdefghijklmnopqrstuvwxyz'
lst = [-1]*26
for w in range(len(word)):
    for i in range(len(alpha)):
        if lst[i] == -1:
           if word[w] == alpha[i]:
               lst[i] = w
print(*lst, sep=' ')