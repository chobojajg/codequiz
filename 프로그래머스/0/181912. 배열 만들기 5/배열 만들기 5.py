def solution(intStrs, k, s, l):
    answer = []
    for i in intStrs:
        check = int(i[s:s+l])
        if check > k:
            answer.append(check)
    return answer