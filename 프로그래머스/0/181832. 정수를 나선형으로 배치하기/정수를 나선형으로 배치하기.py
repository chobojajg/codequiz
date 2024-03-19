def solution(n):
    answer = []
    rv = 1
    cv = 1
    rcnt = 0
    ccnt = 0
    r = -1
    c = 0
    num = 0
    
    for i in range(n):
        answer.append([])
        for j in range(n):
            answer[i].append(0)
            
    while num < n**2:
        if rv == 1 and cv == 1:
            r += rv
            if r == n or answer[c][r] != 0:
                r -= rv
                rv = -1
                num -= 1
            num += 1
            answer[c][r] = num
            continue
        if cv == 1 and rv == -1:
            c += cv
            if c == n or answer[c][r] != 0:
                c -= cv
                cv = -1
                num -= 1
            num += 1
            answer[c][r] = num
            continue
        if rv == -1 and cv == -1:
            r += rv
            if r < 0 or answer[c][r] != 0:
                r -= rv
                rv = 1
                num -= 1
            num += 1
            answer[c][r] = num
            continue
        if cv == -1 and rv == 1:
            c += cv
            if c < 0 or answer[c][r] != 0:
                c -= cv
                cv = 1
                num -= 1
            num += 1
            answer[c][r] = num
            continue
    return answer