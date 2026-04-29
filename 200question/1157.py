sa = 'abcdefghijklmnopqrstuvwxyz'
SA = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lst = [0]*26
word = input()
for w in word:
    for i in range(26):
        if w == SA[i] or w == sa[i]:
            lst[i] += 1
mx, idx, sm = 0, '', -1
for l in range(len(lst)):
    if lst[l] > mx:
        mx = lst[l]
        idx = l
        sm = ''
    elif lst[l] == mx and lst[l] > 0:
        sm = '?'
if sm =='':print(SA[idx])
else:print(sm)