def solution(n):
    answer = 0
    sqrt = n**(1/2)
    if sqrt == int(sqrt):
        return (int(sqrt) + 1)**2
    else:
        return -1