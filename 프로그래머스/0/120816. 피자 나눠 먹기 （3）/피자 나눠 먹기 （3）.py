def solution(slicen, n):
    if n % slicen == 0:
        return n // slicen
    else:
        return (n // slicen) + 1