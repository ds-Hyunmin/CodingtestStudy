word = input()
lst = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
cnt = 0
for l in lst:
    if l in word:
        cnt += word.count(l)
        word = word.replace(l, '.')
word = word.replace('.', '')
print(cnt + len(word))


word = input()
lst = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for l in lst:
    word = word.replace(l, '.')
print(len(word))