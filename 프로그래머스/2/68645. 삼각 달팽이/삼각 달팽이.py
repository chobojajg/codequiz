def solution(n):
    answer = []
    rv = 1
    cv = 1
    r = 0
    c = -1
    num = 0
    result = []
    limit = (n*(n+1))/2

    for i in range(n):
        answer.append([])
        for j in range(n):
            answer[i].append(0)

    while num < limit:
        if rv == 1 and cv == 1:
            c += cv
            if c == n or answer[c][r] != 0:
                c -= cv
                cv = -1
                num -= 1
            num += 1
            answer[c][r] = num
            continue
        if cv == -1 and rv == 1:
            r += rv
            if r == n or answer[c][r] != 0:
                r -= rv
                rv = -1
                num -= 1
            num += 1
            answer[c][r] = num
            continue
        if rv == -1 and cv == -1:
            r += rv
            c += cv
            if r < 0 or answer[c][r] != 0:
                r -= rv
                c -= cv
                rv = 1
                cv = 1
                num -= 1
            num += 1
            answer[c][r] = num
            continue
    for i in range(n):
        for j in range(n):
            if answer[i][j]:
                result.append(answer[i][j])
    return result