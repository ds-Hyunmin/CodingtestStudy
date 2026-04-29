for i in range(int(input())):
    a, b = map(str, input().split())
    for i in b:
        for j in range(int(a)):
            print(i, end='')
