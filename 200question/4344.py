for _ in range(int(input())):
    lst = list(map(int, input().split()))
    num = lst[0]
    lst = lst[1:]
    cnt = 0
    mean = sum(lst)/num
    for i in lst:
        if i > mean:
            cnt += 1
    print('{0}{1}'.format(round(cnt/num*100, 3), '%'))