# 알람 시계
a, b = map(int, input().split())
if b >= 45:b-=45
else:
    if a == 0:a=23
    else:a-=1
    b+=15
print(a, b)