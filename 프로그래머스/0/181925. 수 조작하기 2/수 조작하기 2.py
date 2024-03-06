def solution(numLog):
    answer = []
    for i in range(len(numLog)):
        if i == 0:
            continue
        if numLog[i] - numLog[i-1] == 1: # 1증가
            answer.append('w')
        elif numLog[i] - numLog[i-1] == -1: # 1감소
            answer.append('s')
        elif numLog[i] - numLog[i-1] == 10: # 10증가
            answer.append('d')
        elif numLog[i] - numLog[i-1] == -10: # 10감소
            answer.append('a')
    return ''.join(answer)