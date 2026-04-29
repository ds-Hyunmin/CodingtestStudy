n, m = map(int, input().split())
n_lst, m_lst = [], []
for i in range(n):
    n_lst.append(input())
for i in range(m):
    m_lst.append(input())
m_lst = list(set(m_lst))
print(n+m-len(set(m_lst+n_lst)))

# n, m = map(int, input().split())
# n_lst, cnt = [], 0
# for i in range(n):
#     n_lst.append(input())
# for i in range(m):
#     word = input()
#     if word in n_lst:
#         cnt += 1
# print(cnt)