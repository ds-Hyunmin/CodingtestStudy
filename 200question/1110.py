# n = input()
# if len(n) == 1:
#     n = '0' + n
# rn = n
#
# tmp = str(int(n[0]) + int(n[1]))
# idx_1 = n[-1]
# if len(tmp) == 1:
#     tmp = '0' + tmp
# cnt = 0
# while True: #str(26)과 tmp 값이 같지 않다면
#     a = tmp[-1] #tmp값을 임시저장
#     tmp = str(int(idx_1) + int(tmp[-1])) #새로운 tmp값은 저장해둔 인덱스1값과 tmp값 한자리수 더한 값
#     n = idx_1 + a
#     idx_1 = a #이전tmp값의 인덱스1 값 저장
#
#     cnt += 1
#
#     if len(tmp) == 1: # 새로운 tmp값이 1자리 수라면
#         tmp = '0' + tmp # 앞에 0붙여주기
#
#     if cnt != 0:
#         if rn == n:
#             print(cnt)
#             exit()
#
# print(cnt)

n = input()
if len(n) == 1:
    n = '0' + n

rn = n
cnt = 0

while True:
    # 각 자리 숫자 더하기
    tmp = str(int(n[0]) + int(n[1]))

    # 새로운 수 만들기
    n = n[1] + tmp[-1]

    cnt += 1

    # 원래 수로 돌아오면 종료
    if n == rn:
        break

print(cnt)
