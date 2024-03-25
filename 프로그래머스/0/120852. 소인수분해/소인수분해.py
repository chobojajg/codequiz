def solution(n):
    answer = []
    i = 2
    while n != 1:
        if n % i == 0:
            answer.append(i)
            n /= i
            continue
        i += 1
    answer = list(set(answer))
    answer.sort()
    return answer