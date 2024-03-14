def solution(myStr):
    answer = []
    check = []
    for i in myStr:
        if i == 'a' or i == 'b' or i == 'c':
            if len(check) > 0:
                answer.append(''.join(check))
                check = []
        else:
            check.append(i)
    if len(check) > 0:
        answer.append(''.join(check))
    if len(answer) == 0:
        answer.append('EMPTY')
    return answer