T = int(input())
for test_case in range(1, T + 1):
    s = list(input())
    check = []
    result = 0
    for i in s:
        if i not in check:
            check.append(i)
            result += 1
        else:
            check.remove(i)
            result += 1
        if len(check) == 0:
            result = result // 2
            break

    print(f'#{test_case} {result}')