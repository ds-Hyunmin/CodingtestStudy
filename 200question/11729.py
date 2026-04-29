def hanoi(n, fr, to, aux):
    if n == 1:
        print(fr, to)
        return
    hanoi(n-1, fr, aux, to)
    print(fr, to)
    hanoi(n-1, aux, to, fr)

n = int(input())
hanoi(n, 1, 3, 2 )