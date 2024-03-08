n = int(input())
for _ in range(n):
    x = input()
    check = []
    for i in x:
        if i == ')':
            if '(' in check:
                check.remove('(')
            else:
                check.append(i)
        else:
            check.append(i)
    if len(check) == 0:
        print('YES')
    else:
        print('NO')