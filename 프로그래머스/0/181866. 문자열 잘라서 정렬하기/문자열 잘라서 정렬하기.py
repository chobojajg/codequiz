def solution(myString):
    answer = list(myString.split("x"))
    answer.sort()
    while True:
        if answer[0] == '':
            answer.remove('')
        else:
            break
    return answer