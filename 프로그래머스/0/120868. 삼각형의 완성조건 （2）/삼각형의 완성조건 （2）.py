def solution(sides):
    long = max(sides)
    short = min(sides)
    answer = long + short - (long - short) - 1
    return answer