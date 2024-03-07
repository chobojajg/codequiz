def solution(n):
    answer = 0
    root = n ** (1/2)
    if n == (int(root) ** 2):
        return 1
    else:
        return 2