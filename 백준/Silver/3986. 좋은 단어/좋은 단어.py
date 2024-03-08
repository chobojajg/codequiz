n = int(input())
result = 0
for _ in range(n):
    x = input()
    check = []
    for i in x:
        if len(check) == 0:
            check.append(i)
            continue
        if i == check[-1]:
            check.pop()
        else:
            check.append(i)
    if len(check) == 0:
        result += 1
print(result)