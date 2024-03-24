# def solution(number):
#     return int(number) % 9

def solution(number):
    answer = list(map(int, list(number)))
    sum_answer = sum(answer)
    if sum_answer > 9:
        sum_answer = solution(str(sum_answer))
    elif sum_answer == 9:
        sum_answer = 0
    return sum_answer