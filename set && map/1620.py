# 나는야 포켓몬 마스터 이다솜
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
dic = {}
for i in range(1, n+1):
    dic[i] = input().rstrip('\n')
reversed_dic= dict(map(reversed, dic.items()))
for i in range(m):
    que = input().rstrip('\n')
    try:
        que_int=int(que)
        print(dic.get(que_int))
    except ValueError: print(reversed_dic.get(que))
