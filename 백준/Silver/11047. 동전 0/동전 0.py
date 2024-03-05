n, k = map(int, input().split())
lis = []
for i in range(n):
    lis.append(int(input()))
check = 0
for i in lis[::-1]:
    if i <= k:
        a, k = divmod(k, i)
        check += a
    if k == 0:
        break
print(check)