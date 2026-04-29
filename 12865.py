# n, k=map(int, input().split())
# #n -> 물건의 갯수 k->버틸 수 있는 무게
# dic_w = []
# dic_v = []
# for i in range(n):
#     w, v = map(int, input().split())
#     dic_w.append(w)
#     dic_v.append(v)
# #w -> 각 물건의 무게 v -> 해당 물건의 가치
#
# max = 0
# for j in range(n):
#     cnt = dic_v[j]
#     for h in range(j + 1, n):
#         if dic_w[j] + dic_w[h] < k or dic_w[j] + dic_w[h] == k:
#             cnt += dic_v[h]
#             if cnt > max:
#                 max = cnt
# print(max)
# #2. 버틸 수 있을 만큼의 무게수와 가치를 정렬

n, k=map(int, input().split())
dic_w = []
dic_v = []
for i in range(n):
    w, v = map(int, input().split())
    dic_w.append(w)
    dic_v.append(v)

max = 0
for j in range(n): #n번을 돌면서
    weight = dic_w[j]#weight를 계속 새로 설정해주기
    cnt = dic_v[j]#value_cnt도 설정해주기
    for h in range(j + 1, n):#j+1부터 h까지 범위만..앞 인덱스를 더하는 식의 중복값은 없애려고
        print(j, h)
        if weight + dic_w[h] < k or weight + dic_w[h] == k:#weight + 그다음 인덱스 무게가 같거나 작다면
            cnt += dic_v[h]#밸류에다가도 더해주고
            weight += dic_w[h]#지금 무게에다가도 더해주기
            print(f'{j, h}에서 가치와 무게는 {cnt}, {weight}')
            if cnt > max:#현재 최대값보다 크다면
                print(f'max값은 {max}에서 {cnt}로 갱신')
                max = cnt#최댓값 갱신

print(max)