for _ in range(int(input())):
    h, w, n = map(int, input().split())
    floor = n%h
    room = n//h + 1

    if floor == 0:
        room -= 1
        floor = h
    print(floor*100 + room)

# print(10%5)
# print(10//5)


