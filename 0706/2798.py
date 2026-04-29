# 블랙잭
# n은 입력받는 카드 개수, m은 가장 가까운 합 기준
# 가장 가까운 값 출력이 목표
n, m = map(int, input().split())
cards = list(map(int, input().split()))

tmp = 0
for i in range(len(cards)):
    a = cards[i]
    for j in range(i+1, len(cards)):
        b = cards[j]
        for k in range(j+1, len(cards)):
            c = cards[k]
            if tmp < a + b + c and a + b + c <= m:
                tmp = a + b + c
print(tmp)