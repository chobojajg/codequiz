def solution(l, r):
    answer = []
    lst = []
    check = 0
    while int(format(check, 'b')) <= r // 5:
        lst.append(int(format(check, 'b')))
        check += 1
    print(lst)
    for i in lst:
        a = ''
        for j in str(i):
            a += str(int(j) * 5)
        if l <= int(a) <= r:
            answer.append(int(a))
    if len(answer) == 0:
        answer.append(-1)
    return answer