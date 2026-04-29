#40

a, b = map(str, input().split())
ra, rb = '', ''
for i in range(3):
    ra += a[2-i]
    rb += b[2-i]
print(max(ra, rb))
