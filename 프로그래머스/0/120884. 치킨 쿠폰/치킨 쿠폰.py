def solution(chicken):
    answer = 0
    while chicken >= 10:
        chicken -= 10
        answer += 1
        chicken += 1
    return answer