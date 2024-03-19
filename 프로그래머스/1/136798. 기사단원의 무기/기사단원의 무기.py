def solution(number, limit, power):
    result = 0
    for i in range(1, number + 1):
        answer = 0
        for j in range(1, int(i**(1/2)) + 1):
            if i % j == 0:
                answer += 1
                if j ** 2 != i:
                    answer += 1
        if answer > limit:
            result += power
        else :
            result += answer
    return result