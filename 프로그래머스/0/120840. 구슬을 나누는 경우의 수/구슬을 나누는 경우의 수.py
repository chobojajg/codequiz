facdic = {0:1, 1:1}
def fac(n):
    if n in facdic:
        return facdic[n]
    facdic[n] = n * fac(n - 1)
    return facdic[n]
def solution(balls, share):
    answer = 0
    answer = fac(balls) / (fac(balls - share) * fac(share))
    return answer