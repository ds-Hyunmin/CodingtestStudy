n = int(input())
cnt, tmp = 0, 0
for i in range(666, 10000000):
    if cnt == n:
        print(tmp)
        break
    if '666' in str(i):
        cnt += 1
        tmp = i
