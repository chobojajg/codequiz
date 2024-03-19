def solution(s):
    answer = 0
    temp = []
    check = ''
    cnt = 0
    for i in range(len(s)):
        if len(check) == 0:
            check = s[i]
            temp.append(s[i])
            continue
        if s[i] == check:
            temp.append(s[i])
        else:
            temp.append(s[i])
            cnt += 1
            if temp.count(check) == cnt:
                temp = []
                check = ''
                cnt = 0
                answer += 1
    if len(temp) != 0:
        answer += 1
    return answer