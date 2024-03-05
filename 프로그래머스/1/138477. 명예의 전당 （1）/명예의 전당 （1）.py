def solution(k, score):
    answer = []
    result = []
    for i in score:
        if len(answer) == 0:
            answer.append(i)
        else:
            answer.append(i)
            answer.sort()
        if len(answer) > k:
            answer.pop(0)
        result.append(answer[0])
    return result