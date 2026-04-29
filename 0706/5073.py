# 삼각형과 세 막대

while True:
    lst = list(map(int, input().split()))
    lst.sort(reverse=True)
    a, b, c = lst[0], lst[1], lst[2]

    if lst == [0, 0, 0]:
        break
    if a >= b + c:
        print('Invalid')
    else:
        if a == b == c:
            print('Equilateral')
        elif a == b or b == c:
            print('Isosceles')
        else:
            print('Scalene')