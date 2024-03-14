def solution(strArr):
    answer = {}
    check = []
    for i in strArr:
        if len(i) not in check:
            answer[len(i)] = 0
            check.append(len(i))
        answer[len(i)] += 1
    return max(answer.values())