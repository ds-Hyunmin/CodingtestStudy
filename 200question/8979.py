from pandas import DataFrame
n, m = map(int, input().split())
medal = []
for i in range(n):
    medal.append(list(map(int, input().split())))

medal = DataFrame(axis=1, medal[0])
print(medal)