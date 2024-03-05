def solution(k, m, score):
    answer = []
    result = 0
    less = 0
    for i in range(k, 0, -1):
        a = score.count(i)
        q, r = divmod(a, m)
        result += q * i * m
        print(result)
        less += r
        if less >= m:
            result += i * m
            less -= m

    return result