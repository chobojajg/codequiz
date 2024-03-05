def solution(slicen, n):
    if n % slicen == 0:
        answer = n // slicen
    else:
        answer = (n // slicen) + 1
    return answer