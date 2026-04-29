for i in range(int(input())):
    s, r = map(str, input().split())
    p = ''
    for j in r:
        cnt = 0
        while cnt < int(s):
            p += j
            cnt += 1
    print(p)