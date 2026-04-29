# 최댓값
mx = 0
idx = 0
for i in range(9):
    ans = int(input())
    if i == 0 or ans > mx:
        mx = ans
        idx = i
print(mx)
print(idx+1)