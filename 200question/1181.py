dic = {}
for i in range(int(input())):
    word = input()
    if len(word) in dic.keys():
        dic[len(word)].append(word)
    else:dic[len(word)] = [word]
key_lst = list(dic.items())
key_lst.sort(reverse=False)
for key in key_lst:
    items = list(set(key[1]))
    items.sort(reverse=False)
    for i in items:
        print(i)