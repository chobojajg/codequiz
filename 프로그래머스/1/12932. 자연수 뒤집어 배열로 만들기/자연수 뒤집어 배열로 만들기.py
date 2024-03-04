def solution(n):
    answer = []
    arrstr = list(str(n))
    
    for i in range(len(arrstr)):
        answer.append(int(arrstr[len(arrstr)-i-1]))
    return answer