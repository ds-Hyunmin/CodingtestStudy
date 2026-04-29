import sys
input = sys.stdin.readline
N, A, B = map(int, input().split())
T = sorted(list(map(int, input().split())))
# tt = []
# for i in range(N):
#     cnt = 0
#     for t in T:
#         status = False
#         for x in range(1, A):
#             # print(x)
#             if B*x + A-x <= t:
#                 print(f'B: {B}, x: {x}, A: {A}, t: {t}, B*x + A-x: {B*x + A-x}')
#                 status = True
#         if status: cnt+= 1
#     tt.append(cnt)
# print(tt)

tt = []
for x in range(A):
    sleep = B*x
    t_sleep = sleep
    cnt = 0
    for t in T:
        if t >= A-x + t_sleep:
            cnt += 1
            t_sleep += (A-x)
    if cnt: tt.append(cnt)
    else:
        break
print(tt)
print(max(tt))