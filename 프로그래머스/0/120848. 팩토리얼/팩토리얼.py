def fac(n):
    if n == 0:
        return 1
    return n * fac(n - 1)

def solution(n):
    answer = 1
    p = fac(answer)
    while(p <= n):
        answer += 1
        p = fac(answer)
    answer -= 1
    return answer