import itertools

def solution(number):
    answer = 0
    result = list(itertools.combinations(number, 3))
    for i in result:
        if sum(i) == 0:
            answer += 1
    return answer