def solution(n, k):
    answer = []
    for i in range(int(n/k)):
        answer.append(k*(i+1))
    return answer