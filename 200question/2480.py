# 주사위 세개
a, b, c = map(int, input().split())
lst = [a, b, c]
lst.sort(reverse=False)
if lst[0] == lst[-1]:
    print(10000 + lst[0]*1000)
elif lst[0] == lst[1] or lst[1] == lst[-1]:
    print(1000 + lst[1]*100)
else:
    print(lst[-1]*100)