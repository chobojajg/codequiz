def solution(arr):
    answer = 1
    while len(arr) > answer:
        answer *= 2
    for i in range(answer - len(arr)):
        arr.append(0)
    return arr