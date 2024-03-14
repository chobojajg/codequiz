def solution(emergency):
    answer = emergency[:]
    lis = emergency[:]
    emergency.sort(reverse = True)
    for i in range(len(emergency)):
        answer[lis.index(emergency[i])] = i + 1
    return answer